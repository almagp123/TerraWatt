# # %%
# import sys

import urllib3
# %%
from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "Q8bleCO5jiX1y=-0Pk*L"),
    verify_certs=False
)

# %%
client.info()
client.cat.indices(s='index', format='json')

# %%
list(client.cat.indices(s='index', format='json'))

# %%
# Consultar los índices existentes
existing_indices = client.cat.indices(format="json")
index_names = [index["index"] for index in existing_indices]

# Crear un nuevo índice solo si no existe
new_index_name = "modelo_consumo_met_fest_python"
if new_index_name not in index_names:
    client.indices.create(index=new_index_name)
    print(f"Índice '{new_index_name}' creado exitosamente.")
else:
    print(f"El índice '{new_index_name}' ya existe.")


# %%
import pandas as pd
from elasticsearch.helpers import bulk

# Cargar el archivo CSV
df = pd.read_csv("./Modelo_Consumo_Met_fest.csv", delimiter=';')

# Crear una lista de documentos para el bulk
actions = []

for index, row in df.iterrows():
    # Crear cada documento en el formato esperado por Elasticsearch
    doc = {
        "_index": "modelo_consumo_met_fest", 
        "_id": f"modelo_consumo_{index}", 
        "_source": {
            "Fecha": row["Fecha"],
            "Provincia": row["Provincia"],
            "Consumo_energetico": row["Consumo energético (kWh/m²)"],
            "Media_residentes": row["Media de residentes"],
            "Potencia_contratada": row["Potencia contratada (kW)"],
            "Tipo_vivienda": row["Tipo de vivienda"],
            "Altitud": row["ALTITUD"],
            "TMedia": row["TMEDIA"],
            "TMin": row["TMIN"],
            "TMax": row["TMAX"],
            "Dir": row["DIR"],
            "VelMedia": row["VELMEDIA"],
            "Racha": row["RACHA"],
            "Sol": row["SOL"],
            "PresMax": row["PRESMAX"],
            "PresMin": row["PRESMIN"],
            "Festivo": row["Festivo"],
            "Entre_semana": row["Entre semana"]
        }
    }
    # Añadir el documento a la lista de acciones
    actions.append(doc)

    # Mostrar progreso cada 500 documentos
    if index % 500 == 0:
        print(f"Preparados {index} documentos para el bulk")

# Enviar todos los documentos a Elasticsearch usando el bulk
response = bulk(client, actions)
print(f"Bulk completado. {len(actions)} documentos indexados.")


# %%
# Consultar los índices existentes
existing_indices = client.cat.indices(format="json")
index_names = [index["index"] for index in existing_indices]

# Crear un nuevo índice solo si no existe
new_index_name = "modelo_precios_met_fest_python"
if new_index_name not in index_names:
    client.indices.create(index=new_index_name)
    print(f"Índice '{new_index_name}' creado exitosamente.")
else:
    print(f"El índice '{new_index_name}' ya existe.")


# %%
import pandas as pd
from elasticsearch.helpers import bulk

# Cargar el archivo CSV
df = pd.read_csv("./Modelo_Precios_Met_Fest.csv", delimiter=';')

# Crear una lista de documentos para el bulk
actions = []

for index, row in df.iterrows():
    # Crear cada documento en el formato esperado por Elasticsearch
    doc = {
        "_index": "modelo_precios_met_fest_python",  # Nombre del índice
        "_id": f"modelo_precios_{index}",  # ID único por documento
        "_source": {
            "Fecha": row["FECHA"],
            "Provincia": row["Provincia"],
            "Altitud": row["ALTITUD"],
            "TMedia": row["TMEDIA"],
            "TMin": row["TMIN"],
            "TMax": row["TMAX"],
            "Dir": row["DIR"],
            "VelMedia": row["VELMEDIA"],
            "Racha": row["RACHA"],
            "Sol": row["SOL"],
            "PresMax": row["PRESMAX"],
            "PresMin": row["PRESMIN"],
            "Precio_total_con_impuestos": row["Precio total con impuestos (€/MWh)"],
            "Festivo": row["Festivo"],
            "Entre_semana": row["Entre semana"]
        }
    }
    # Añadir el documento a la lista de acciones
    actions.append(doc)

    # Mostrar progreso cada 500 documentos
    if index % 500 == 0:
        print(f"Preparados {index} documentos para el bulk")

# Enviar todos los documentos a Elasticsearch usando el bulk
response = bulk(client, actions)
print(f"Bulk completado. {len(actions)} documentos indexados.")


# %% [markdown]
# Para comprobar que esta bien cargado realizaremos una consulta de prueba

# %%
# # Consultar los primeros 10 documentos del índice
# search_response = client.search(
#     index=new_index_name,
#     body={"query": {"match_all": {}}, "size": 10}
# )
# for doc in search_response["hits"]["hits"]:
#     print(doc["_source"])



