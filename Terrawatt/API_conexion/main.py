# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI
# from pydantic import BaseModel
# import os
# import pandas as pd
# import joblib
# from sklearn.preprocessing import StandardScaler




# class Datos(BaseModel):
#     potencia: float
#     numero_residentes: float
#     tipo_vivienda: str
#     provincia: str
#     mes: int  # Añadir el nuevo campo mes
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # En producción, restringe los orígenes permitidos
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
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



# # Modelo bueno arriba

# # ----------

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import calendar
from datetime import datetime
import numpy as np

# Crear la instancia de la API y configurar CORS
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para producción: restringir orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definir el modelo de entrada para el endpoint de transformación
class Datos(BaseModel):
    potencia: float
    numero_residentes: float
    tipo_vivienda: str
    provincia: str
    mes: int  # Mes (número 1-12)

RUTA_METEOROLOGICA = "../Limpieza_datos/Datos_limpios_meteorologicos"

@app.post("/transformar")
async def transformar_datos(datos: Datos):
    # ---------------------------
    # Parte 1: Predicción de Consumo
    # ---------------------------
    # Variables dummies para el tipo de vivienda
    tipos_vivienda = [
        'Tipo de vivienda_Adosado',
        'Tipo de vivienda_Casa Unifamiliar',
        'Tipo de vivienda_Duplex',
        'Tipo de vivienda_Piso'
    ]
    variables_vivienda = {tipo: False for tipo in tipos_vivienda}
    if datos.tipo_vivienda == "Adosado":
        variables_vivienda['Tipo de vivienda_Adosado'] = True
    elif datos.tipo_vivienda == "Casa Unifamiliar":
        variables_vivienda['Tipo de vivienda_Casa Unifamiliar'] = True
    elif datos.tipo_vivienda == "Duplex":
        variables_vivienda['Tipo de vivienda_Duplex'] = True
    elif datos.tipo_vivienda == "Piso":
        variables_vivienda['Tipo de vivienda_Piso'] = True
    else:
        return {"error": "Tipo de vivienda no reconocido. Por favor, revisa tu entrada."}

    # Cargar y filtrar datos meteorológicos
    provincia = datos.provincia
    archivo_provincia = os.path.join(RUTA_METEOROLOGICA, f"{provincia}.csv")
    if not os.path.exists(archivo_provincia):
        return {"error": f"No se encontró el archivo de la provincia: {provincia}"}

    df_meteorologico = pd.read_csv(archivo_provincia, delimiter=";")
    df_meteorologico["MES"] = pd.to_datetime(df_meteorologico["FECHA"]).dt.month
    df_filtrado = df_meteorologico[df_meteorologico["MES"] == datos.mes]
    columnas_meteorologicas = ["TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN"]
    medias_meteorologicas = df_filtrado[columnas_meteorologicas].mean()
    medias_dict = medias_meteorologicas.to_dict()

    # Construir datos transformados (para el modelo de consumo)
    datos_transformados = {
        "potencia": datos.potencia,
        "numero_residentes": datos.numero_residentes,
        "provincia": datos.provincia,
        "mes": datos.mes,
    }
    datos_transformados = {**datos_transformados, **medias_dict, **variables_vivienda}

    # Cargar el modelo de consumo (formato .pkl)
    RUTA_MODELOS = "../modelos_guardados"
    modelo_path = os.path.join(RUTA_MODELOS, f"Modelo_{provincia}.pkl")
    if not os.path.exists(modelo_path):
        print(f"El modelo para {provincia} no se encontró en la ruta: {modelo_path}")
        return {"error": f"No se encontró el modelo para la provincia: {provincia}"}
    modelo_consumo = joblib.load(modelo_path)

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
        datos.potencia,
        datos.mes,
        datos.numero_residentes,
        datos_transformados["Tipo de vivienda_Adosado"],
        datos_transformados["Tipo de vivienda_Casa Unifamiliar"],
        datos_transformados["Tipo de vivienda_Duplex"],
        datos_transformados["Tipo de vivienda_Piso"]
    ]
    features_df = pd.DataFrame([features], columns=feature_names)
    scaler = StandardScaler()
    features_to_normalize = ["TMEDIA", "TMIN", "TMAX", "VELMEDIA", "SOL", "PRESMAX", "PRESMIN", "Potencia contratada (kW)"]
    features_df[features_to_normalize] = scaler.fit_transform(features_df[features_to_normalize])

    # Depuración: Imprimir los datos enviados al modelo de consumo
    print("=== Datos enviados al modelo de consumo ===")
    print(features_df.to_string())

    # Realizar la predicción de consumo
    prediccion_consumo = modelo_consumo.predict(features_df)
    prediccion_consumo = max(0, prediccion_consumo[0])
    datos_transformados["prediccion_consumo"] = prediccion_consumo

    # ---------------------------
    # Parte 2: Predicción de Precio (por intervalo de fechas)
    # ---------------------------
    # Suponemos que se dispone de un modelo de precios entrenado y guardado en formato .pkl
    # (por ejemplo, un MLPRegressor) en la ruta "../modelos_guardados/AModelo_precios_mlp.pkl"
    modelo_precios_path = os.path.join(RUTA_MODELOS, "AModelo_precios_mlp.pkl")
    if os.path.exists(modelo_precios_path):
        modelo_precios = joblib.load(modelo_precios_path)
        
        # Para determinar el intervalo: usaremos como año 2025 (por ejemplo)
        # Usamos el mes (datos.mes) para definir el primer y último día
        año = 2025
        fecha_inicio = datetime(año, datos.mes, 1)
        ultimo_dia = calendar.monthrange(año, datos.mes)[1]
        fecha_fin = datetime(año, datos.mes, ultimo_dia)
        
        # Generar rango de fechas diario
        rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='D')
        n_dias = len(rango_fechas)
        print(f"Prediciendo precio para {n_dias} días, de {fecha_inicio.strftime('%Y-%m-%d')} a {fecha_fin.strftime('%Y-%m-%d')}.")

        # Cargar el dataset de precios para obtener el último precio histórico para la provincia
        # (Se asume que el archivo es el mismo que usaste para entrenar el modelo de precios)
        file_path_precios = "../Limpieza_datos/Modelo_Precios_Met_Fest.csv"
        data_precios = pd.read_csv(file_path_precios, delimiter=';')
        data_precios['FECHA'] = pd.to_datetime(data_precios['FECHA'])
        data_precios = data_precios.sort_values(by='FECHA')
        data_provincia_precios = data_precios[data_precios['Provincia'].str.upper() == provincia.upper()]
        if data_provincia_precios.empty:
            return {"error": f"No se encontraron datos de precios para la provincia: {provincia}"}
        ultimo_precio = data_provincia_precios['Precio total con impuestos (€/MWh)'].values[-1]
        print("Último precio histórico para predicción de precios:", ultimo_precio)

        # Predicción recursiva: se usa el último precio conocido para predecir cada día
        predicciones_precio = []
        precio_actual = ultimo_precio
        for dia in rango_fechas:
            # El modelo de precios espera una entrada de forma (n_samples, 1)
            entrada_precio = np.array([[precio_actual]])
            precio_siguiente = modelo_precios.predict(entrada_precio)[0]
            predicciones_precio.append(precio_siguiente)
            precio_actual = precio_siguiente  # actualizar para la siguiente iteración

        precio_medio = np.mean(predicciones_precio)
        # Agregar a los datos transformados la información de la predicción del precio
        datos_transformados["precio"] = {
            "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
            "precio_medio": precio_medio,
            "predicciones_diarias": predicciones_precio  # opcional
        }
    else:
        datos_transformados["precio"] = "Modelo de precios no disponible"

    # Retornar los resultados de consumo y precio
    return {"datos_transformados": datos_transformados}
