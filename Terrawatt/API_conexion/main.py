from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler



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

# class Datos(BaseModel):
#     potencia: float
#     numero_residentes: float
#     tipo_vivienda: str
#     provincia: str
#     mes: int  # Añadir el nuevo campo mes


# RUTA_METEOROLOGICA = "../Limpieza_datos/Datos_limpios_meteorologicos"

# # Endpoint
# @app.post("/transformar")
# async def transformar_datos(datos: Datos):
#     # Definir todas las posibles variables dummies para el tipo de vivienda
#     tipos_vivienda = [
#         'Tipo de vivienda_Adosado',
#         'Tipo de vivienda_Casa Unifamiliar',
#         'Tipo de vivienda_Duplex',
#         'Tipo de vivienda_Piso'
#     ]

#     # Crear un diccionario con todas las variables inicialmente en 0
#     variables_vivienda = {tipo: False for tipo in tipos_vivienda}

#     # Asignar el valor 1 a la variable correspondiente según el tipo de vivienda
#     if datos.tipo_vivienda == "Adosado":
#         variables_vivienda['Tipo de vivienda_Adosado'] = True
#     elif datos.tipo_vivienda == "Casa Unifamiliar":
#         variables_vivienda['Tipo de vivienda_Casa Unifamiliar'] = True
#     elif datos.tipo_vivienda == "Duplex":
#         variables_vivienda['Tipo de vivienda_Duplex'] = True
#     elif datos.tipo_vivienda == "Piso":
#         variables_vivienda['Tipo de vivienda_Piso'] = True
#     else:
#         return {"error": "Tipo de vivienda no reconocido. Por favor, revisa tu entrada."}



#     provincia = datos.provincia  # Nombre de la provincia
#     archivo_provincia = os.path.join(RUTA_METEOROLOGICA, f"{provincia}.csv")
#     df_meteorologico = pd.read_csv(archivo_provincia, delimiter=";")
#     df_meteorologico["MES"] = pd.to_datetime(df_meteorologico["FECHA"]).dt.month
#     mes_usuario = datos.mes
#     df_filtrado = df_meteorologico[df_meteorologico["MES"] == mes_usuario]

#     columnas_meteorologicas = ["TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN"]

#     medias_meteorologicas = df_filtrado[columnas_meteorologicas].mean()
#     medias_dict = medias_meteorologicas.to_dict()


#     # Convertir las medias a un diccionario
#     medias_dict = medias_meteorologicas.to_dict()
 



        
#     if not os.path.exists(archivo_provincia):
#         return {"error": f"No se encontró el archivo de la provincia: {provincia}"}
#     # Construir los datos transformados
#     datos_transformados = {
#         "potencia": datos.potencia,
#         "numero_residentes": datos.numero_residentes ,
#         "provincia": datos.provincia,
#         "mes": datos.mes,  
#     }

#     datos_transformados = {**datos_transformados,  **medias_dict, **variables_vivienda}



#     RUTA_MODELOS = "../modelos_guardados"
#     modelo_path = os.path.join(RUTA_MODELOS, f"Modelo_{provincia}.pkl")

    
#     if not os.path.exists(modelo_path):
#         print(f"El modelo para {provincia} no se encontró en la ruta: {modelo_path}")

#         return {"error": f"No se encontró el modelo para la provincia: {provincia},,, El modelo para {provincia} no se encontró en la ruta: {modelo_path}"}
    
#     modelo = joblib.load(modelo_path)


#     feature_names = [
#         "TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN",
#         "Potencia contratada (kW)", "Mes", "Media de residentes",
#         "Tipo de vivienda_Adosado", "Tipo de vivienda_Casa Unifamiliar", 
#         "Tipo de vivienda_Duplex", "Tipo de vivienda_Piso"
#     ]
#     # Preparar los datos para la predicción (asegúrate de que estén en el formato adecuado)
#     features = [
#         datos_transformados["TMEDIA"],
#         datos_transformados["TMIN"],
#         datos_transformados["TMAX"],
#         datos_transformados["VELMEDIA"],
#         datos_transformados["SOL"],
#         datos_transformados["PRESMAX"],
#         datos_transformados["PRESMIN"],
#         datos.potencia,  # Potencia contratada (kW)
#         datos.mes,  # Mes
#         datos.numero_residentes,  # Media de residentes
#         datos_transformados["Tipo de vivienda_Adosado"],
#         datos_transformados["Tipo de vivienda_Casa Unifamiliar"],
#         datos_transformados["Tipo de vivienda_Duplex"],
#         datos_transformados["Tipo de vivienda_Piso"]
#     ]
#     features_df = pd.DataFrame([features], columns=feature_names)

#     # Normalizar solo las columnas numéricas necesarias
#     scaler = StandardScaler()

#     # Variables que necesitan ser normalizadas
#     features_to_normalize = ["TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN", "Potencia contratada (kW)"]

#     # Normalizar las columnas seleccionadas
#     features_df[features_to_normalize] = scaler.fit_transform(features_df[features_to_normalize])

#     # Realizar la predicción
#     prediccion = modelo.predict(features_df)

#     # Ajustar la predicción si es negativa
#     prediccion = max(0, prediccion[0])

#     datos_transformados = {**datos_transformados, **medias_dict, **variables_vivienda, "prediccion": prediccion}


#     return {"datos_transformados": datos_transformados}


import pandas as pd
import numpy as np
import joblib
import os
# from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI
from pydantic import BaseModel

# Función para la predicción LSTM
def predecir_precio_medio_intervalo(provincia, fecha_inicio, fecha_fin, data):
    # Generar rango de fechas
    dias_intervalo = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='D')

    # Filtrar los datos para la provincia
    data_provincia = data[data['Provincia'].str.upper() == provincia.upper()]

    if data_provincia.empty:
        raise ValueError(f"No se encontraron datos para la provincia {provincia}. Por favor, revisa el nombre.")

    # Obtener el último valor disponible como punto de partida
    ultimo_valor = data_provincia['Precio total con impuestos (€/MWh)'].values[-1]
    valor_inicial = np.array([[ultimo_valor]]).reshape(1, 1, 1)

    # Predicciones para cada día en el intervalo
    predicciones = []
    for _ in dias_intervalo:
        prediccion = modelo_lstm.predict(valor_inicial).flatten()[0]
        predicciones.append(max(prediccion, 0))  # Asegurarse de que no haya valores negativos
        valor_inicial = np.array([[prediccion]]).reshape(1, 1, 1)

    # Calcular el precio medio
    precio_medio_intervalo = np.mean(predicciones)
    return precio_medio_intervalo


# Función para la predicción con scikit-learn
def predecir_precio_scikit(datos_transformados, provincia):
    # Cargar el modelo de la provincia
    modelo_path = f"../modelos_guardados/Modelo_{provincia}.pkl"
    
    if not os.path.exists(modelo_path):
        raise ValueError(f"No se encontró el modelo para la provincia {provincia}")

    modelo = joblib.load(modelo_path)

    # Crear el dataframe con las características para hacer la predicción
    feature_names = [
        "TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN",
        "Potencia contratada (kW)", "Mes", "Media de residentes",
        "Tipo de vivienda_Adosado", "Tipo de vivienda_Casa Unifamiliar", 
        "Tipo de vivienda_Duplex", "Tipo de vivienda_Piso"
    ]

    features = [
        datos_transformados["TMEDIA"],
        datos_transformados["TMIN"],
        datos_transformados["TMAX"],
        datos_transformados["VELMEDIA"],
        datos_transformados["SOL"],
        datos_transformados["PRESMAX"],
        datos_transformados["PRESMIN"],
        datos_transformados["potencia"],  # Potencia contratada (kW)
        datos_transformados["mes"],  # Mes
        datos_transformados["numero_residentes"],  # Media de residentes
        datos_transformados["Tipo de vivienda_Adosado"],
        datos_transformados["Tipo de vivienda_Casa Unifamiliar"],
        datos_transformados["Tipo de vivienda_Duplex"],
        datos_transformados["Tipo de vivienda_Piso"]
    ]

    features_df = pd.DataFrame([features], columns=feature_names)

    # Normalizar solo las columnas numéricas necesarias
    scaler = StandardScaler()
    features_to_normalize = ["TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN", "Potencia contratada (kW)"]

    features_df[features_to_normalize] = scaler.fit_transform(features_df[features_to_normalize])

    # Realizar la predicción
    prediccion = modelo.predict(features_df)

    # Ajustar la predicción si es negativa
    prediccion = max(0, prediccion[0])
    
    return prediccion


# FastAPI app
app = FastAPI()

class Datos(BaseModel):
    potencia: float
    numero_residentes: float
    tipo_vivienda: str
    provincia: str
    mes: int

# Cargar los datos meteorológicos
data = pd.read_csv("../Limpieza_datos/Modelo_Precios_Met_Fest.csv", delimiter=';')
data['FECHA'] = pd.to_datetime(data['FECHA'])

@app.post("/transformar")
async def transformar_datos(datos: Datos):
    # Determinar la fecha de inicio y fin según el mes
    mes = datos.mes
    fecha_inicio = f"2025-{mes:02d}-01"
    if mes == 2:
        fecha_fin = "2025-02-28"
    elif mes in [4, 6, 9, 11]:
        fecha_fin = f"2025-{mes:02d}-30"
    else:
        fecha_fin = f"2025-{mes:02d}-31"

    # Filtrar datos meteorológicos y calcular medias
    provincia = datos.provincia
    precio_medio = predecir_precio_medio_intervalo(provincia, fecha_inicio, fecha_fin, data)
    
    # Transformación de los datos y predicción con scikit-learn o LSTM
    try:
        if provincia in ["ALAVA", "OTRAS PROVINCIAS"]:  # Define las provincias donde se usará scikit-learn
            prediccion = predecir_precio_scikit(datos.dict(), provincia)
        else:  # Para otras provincias, se usará el modelo LSTM
            prediccion = precio_medio
    except ValueError as e:
        return {"error": str(e)}

    # Formato de salida
    return {"prediccion": prediccion, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin}
