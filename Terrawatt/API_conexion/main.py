from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (ajusta esto en producción)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

from pydantic import BaseModel

# # Modificar la clase Datos para reflejar los cambios
# class Datos(BaseModel):
#     potencia: float
#     numero_residentes: int
#     tipo_vivienda: str
#     provincia: str
#     mes: str  # Añadir el nuevo campo mes

# # Endpoint
# @app.post("/transformar")
# async def transformar_datos(datos: Datos):
#     datos_transformados = {
#         "potencia": datos.potencia + 100,
#         "numero_residentes": datos.numero_residentes + 100,
#         "tipo_vivienda": f"hola {datos.tipo_vivienda}",
#         "provincia": f"hola {datos.provincia}",
#         "mes": f"Mes seleccionado: {datos.mes}",  # Modificar para reflejar el mes
#     }
#     return {"datos_transformados": datos_transformados}



import joblib
import os
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Definir el modelo de entrada
class Datos(BaseModel):
    potencia: float
    numero_residentes: int
    tipo_vivienda: str
    provincia: str
    mes: int  # Mes seleccionado por el usuario

# Ruta para los modelos guardados
modelos_guardados_folder = "C:/Users/Alma/Desktop/TerraWatt/Terrawatt/modelos_guardados"
# Ruta para los archivos meteorológicos
datos_meteorologicos_folder = "C:/Users/Alma/Desktop/TerraWatt/Terrawatt/Limpieza_datos/Datos_limpios_meteorologicos"

# Función para cargar el modelo correspondiente a la provincia
def cargar_modelo(provincia):
    modelo_filename = os.path.join(modelos_guardados_folder, f"Modelo_{provincia}.pkl")
    if os.path.exists(modelo_filename):
        return joblib.load(modelo_filename)
    else:
        raise FileNotFoundError(f"El modelo para la provincia {provincia} no se encuentra disponible.")

# Función para cargar los datos meteorológicos correspondientes
def cargar_datos_meteorologicos(provincia, mes):
    archivo_datos = os.path.join(datos_meteorologicos_folder, f"Datos_Meteorologicos_{provincia}.csv")
    if os.path.exists(archivo_datos):
        # Cargar los datos
        datos = pd.read_csv(archivo_datos)
        
        # Convertir la columna 'Fecha' a tipo datetime
        datos['FECHA'] = pd.to_datetime(datos['FECHA'], errors='coerce')
        
        # Filtrar los datos para el mes seleccionado
        datos_mes = datos[datos['FECHA'].dt.month == mes]
        
        # Calcular la media de las columnas numéricas meteorológicas para el mes seleccionado
        datos_mes_media = datos_mes[['TMEDIA', 'TMIN', 'TMAX', 'VELMEDIA', 'SOL', 'PRESMAX', 'PRESMIN']].mean()
        
        return datos_mes_media
    else:
        raise FileNotFoundError(f"Los datos meteorológicos para la provincia {provincia} no se encuentran disponibles.")

# Endpoint para hacer la predicción
@app.post("/transformar")
async def transformar_datos(datos: Datos):
    # Obtener la provincia y el mes de los datos enviados
    provincia = datos.provincia
    mes = datos.mes

    try:
        # Cargar el modelo correspondiente a la provincia
        modelo = cargar_modelo(provincia)

        # Cargar los datos meteorológicos correspondientes a la provincia y mes
        datos_meteorologicos = cargar_datos_meteorologicos(provincia, mes)
        
        # Aquí puedes preparar los datos meteorológicos junto con los otros datos que recibes (como potencia, etc.)
        # Asumiendo que tienes los datos meteorológicos calculados como media:
        X_entrada = [
            datos.potencia,
            datos.numero_residentes,
            datos.tipo_vivienda,
            datos_meteorologicos['TMEDIA'],  # Media de TMEDIA
            datos_meteorologicos['TMIN'],    # Media de TMIN
            datos_meteorologicos['TMAX'],    # Media de TMAX
            datos_meteorologicos['VELMEDIA'],# Media de VELMEDIA
            datos_meteorologicos['SOL'],     # Media de SOL
            datos_meteorologicos['PRESMAX'], # Media de PRESMAX
            datos_meteorologicos['PRESMIN']  # Media de PRESMIN
        ]
        
        # Realizar la predicción
        prediccion = modelo.predict([X_entrada])

        # Devolver la predicción
        return {"prediccion": prediccion.tolist()}  # Devolver el resultado como una lista

    except FileNotFoundError as e:
        return {"error": str(e)}
