# %% [markdown]
# Como hemos hecho en el notebook de los datos meteorologicos vamos primeramente a obtener los nombres de las provincias para poder ver si alguna errata o alguna duplicada, de todos modos vamos a usar un diccionario tmbién para que tengan exactamente el mismo nombre que en el dataset de los datos meteorologico.

# %%
import pandas as pd
import os
import unidecode
file_path = "Datos_brutos_generales/Consumo_Energetico_Viviendas.csv"

try:
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8', engine='python')

    # Verificar si la columna "Provincia" existe
    if "Provincia" in df.columns:
        # Obtener las provincias únicas
        provincias_unicas = df["Provincia"].dropna().unique()

        # Mostrar las provincias únicas ordenadas alfabéticamente
        print("Provincias únicas encontradas:")
        for provincia in sorted(provincias_unicas):
            print(provincia)
    else:
        print("La columna 'Provincia' no existe en el archivo.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")


# %% [markdown]
# Como podemos ver hay varias de ellas que no reconocer correctamente, por lo que sustituimos por los mismos nombres que hemos utilizado en el anterior dataset

# %%
import os
import pandas as pd
import unidecode

file_path = "Datos_brutos_generales/Consumo_Energetico_Viviendas.csv"

# Verificar si el archivo existe antes de intentar leerlo
if not os.path.exists(file_path):
    print(f"El archivo {file_path} no existe.")
else:
    # Leer el archivo CSV
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8', engine='python')

    # Verificar y transformar la columna 'Provincia'
    if "Provincia" in df.columns:
        df["Provincia"] = df["Provincia"].apply(lambda x: unidecode.unidecode(x).upper().strip())

    # Crear la carpeta si no existe
    output_folder = "Datos_limpios_generales"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Carpeta creada: {output_folder}")

    # Guardar el archivo actualizado
    output_path = os.path.join(output_folder, "Consumo_Energetico_Viviendas_Limpio.csv")
    df.to_csv(output_path, sep=';', index=False, encoding='utf-8')

    print(f"Archivo actualizado guardado en: {output_path}")

    # Verificar las provincias únicas después de la corrección
    provincias_corregidas = df["Provincia"].dropna().unique()

    for provincia in sorted(provincias_corregidas):
        print(provincia)


# %% [markdown]
# Comprobamos que para ambos csv que vamos a unir tienen los mismos nombres de las provincias, para no tener ningun tipo de problema cuando las vayamos a unir, además te escribe que provincias no son semejantes en caso de que haya.

# %%
consumo_file = "Datos_limpios_generales/Consumo_Energetico_Viviendas_Limpio.csv"
meteorologicos_folder = "Datos_limpios_meteorologicos"

try:
    consumo_df = pd.read_csv(consumo_file, delimiter=';', encoding='latin1', engine='python')
    provincias_consumo = set(consumo_df["Provincia"].dropna().unique())
except Exception as e:
    print(f"Error leyendo el archivo {consumo_file}: {e}")
    provincias_consumo = set()

provincias_meteorologicos = set()

try:
    for file_name in os.listdir(meteorologicos_folder):
        if file_name.endswith(".csv"):  
            # Extraer el nombre de la provincia desde el nombre del archivo (sin extensión)
            provincia = os.path.splitext(file_name)[0].upper() 
            provincias_meteorologicos.add(provincia)
except Exception as e:
    print(f"Error leyendo los archivos en la carpeta {meteorologicos_folder}: {e}")

# Comparar las provincias entre ambos conjuntos
provincias_faltantes_en_consumo = provincias_meteorologicos - provincias_consumo
provincias_faltantes_en_meteorologicos = provincias_consumo - provincias_meteorologicos

# Mostrar los resultados
print("\nProvincias presentes en Datos_limpios_meteorologicos pero no en Consumo_Energetico_Viviendas_Corregido:")
for provincia in sorted(provincias_faltantes_en_consumo):
    print(provincia)

print("\nProvincias presentes en Consumo_Energetico_Viviendas_Corregido pero no en Datos_limpios_meteorologicos:")
for provincia in sorted(provincias_faltantes_en_meteorologicos):
    print(provincia)



# %% [markdown]
# Como podemos ver no coinciden todas así que vamos a hacer un mapeo de aquellas no coincidan 

# %%
# Leer el archivo CSV
file_path = "Datos_limpios_generales/Consumo_Energetico_Viviendas_Limpio.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8', engine='python')

# Diccionario de mapeo para corregir los nombres de las provincias
mapeo_provincias = {
    "BALEARES": "ILLES BALEARS",
    "GERONA": "GIRONA",
    "GUIPUZCOA": "GIPUZKOA",
    "LA CORUNA": "A CORUÑA",
    "LERIDA": "LLEIDA",
    "ORENSE": "OURENSE",
    "VIZCAYA": "BIZKAIA"
}

# Aplicar el mapeo a la columna "Provincia"
if "Provincia" in df.columns:
    df["Provincia"] = df["Provincia"].replace(mapeo_provincias)

# Guardar el archivo actualizado
df.to_csv(file_path, sep=';', index=False, encoding='utf-8')

print(f"Archivo corregido guardado en: {file_path}")

# %% [markdown]
# Generamos el dataset del primer modelo ya que vamos a realizar dos modelos, uno para la prediccion del precio de la electricidad y otro para la prediccion del consumo. En este caso para como ya tenemos copiado en el modelo los datos de consumo ahora vamos a añadir los datos metereologicos 

# %%
modelo_path = "Datos_limpios_generales/Consumo_Energetico_Viviendas_Limpio.csv"
meteorologicos_folder = "Datos_limpios_meteorologicos"
output_path = 'Modelo_Consumo_Met_fest.csv'

df_modelo = pd.read_csv(modelo_path, delimiter=';', encoding='utf-8')

df_resultado = pd.DataFrame()

for file_name in os.listdir(meteorologicos_folder):
    if file_name.endswith(".csv"): 
        provincia = file_name.replace(".csv", "").upper()  # Obtener el nombre de la provincia desde el archivo
        meteorologico_path = os.path.join(meteorologicos_folder, file_name)
        
        # Leer el archivo meteorológico
        df_meteorologico = pd.read_csv(meteorologico_path, delimiter=';', encoding='utf-8')
        
        # Convertir la columna FECHA a datetime
        if 'FECHA' in df_meteorologico.columns:
            df_meteorologico['FECHA'] = pd.to_datetime(df_meteorologico['FECHA'], format='%Y-%m-%d', errors='coerce')
        
        # Filtrar las filas de modelo para la provincia actual
        df_modelo_provincia = df_modelo[df_modelo['Provincia'].str.upper() == provincia].copy()
        
        # Si hay datos para la provincia en el modelo
        if not df_modelo_provincia.empty:
            # Convertir la columna Fecha a datetime
            if 'Fecha' in df_modelo_provincia.columns:
                df_modelo_provincia['Fecha'] = pd.to_datetime(df_modelo_provincia['Fecha'], format='%Y-%m-%d', errors='coerce')
            
            # Unir los datos meteorológicos con el modelo usando la fecha
            df_combinado = pd.merge(df_modelo_provincia, df_meteorologico, how='left', left_on='Fecha', right_on='FECHA')
            
            # Añadir los datos combinados al resultado
            df_resultado = pd.concat([df_resultado, df_combinado], ignore_index=True)

# Eliminar la columna duplicada 'FECHA' si existe en el resultado
if 'FECHA' in df_resultado.columns:
    df_resultado = df_resultado.drop(columns=['FECHA'])

# Guardar el archivo combinado
df_resultado.to_csv(output_path, sep=';', index=False, encoding='utf-8')
print(f"Archivo combinado guardado en: {output_path}")


# %% [markdown]
# Añadimos las variables de si es festivo y si es un día entre semana.

# %%
# Rutas de los archivos
consumo_path = "Modelo_Consumo_Met_fest.csv"
festivos_path = "Datos_brutos_generales/Festivos.csv"

# Leer los datasets
df_consumo = pd.read_csv(consumo_path, delimiter=';', encoding='utf-8')
df_festivos = pd.read_csv(festivos_path, delimiter=';', encoding='utf-8')

# Estandarizar las columnas "Provincia" y "Fecha"
df_consumo["Provincia"] = df_consumo["Provincia"].str.strip().str.upper()
df_festivos["Provincia"] = df_festivos["Provincia"].str.strip().str.upper()

# Convertir las fechas de ambos datasets al mismo formato
df_consumo["Fecha"] = pd.to_datetime(df_consumo["Fecha"], format='%Y-%m-%d', errors='coerce')
df_festivos["Fecha"] = pd.to_datetime(df_festivos["Fecha"], format='%d/%m/%Y', errors='coerce')

# Crear una clave de combinación basada en Fecha y Provincia
df_consumo["Clave"] = df_consumo["Fecha"].astype(str) + "_" + df_consumo["Provincia"]
df_festivos["Clave"] = df_festivos["Fecha"].astype(str) + "_" + df_festivos["Provincia"]

# Añadir la columna "Festivo" al dataset de consumo
df_consumo["Festivo"] = df_consumo["Clave"].isin(df_festivos["Clave"]).map({True: "SI", False: "NO"})

# Añadir la columna "Día de la semana"
# 0 = Lunes, ..., 4 = Viernes (Entre semana), 5 = Sábado, 6 = Domingo (Fin de semana)
df_consumo["Entre semana"] = df_consumo["Fecha"].dt.dayofweek.apply(lambda x: "SI" if x < 5 else "NO")

# Eliminar la columna auxiliar "Clave"
df_consumo.drop(columns=["Clave"], inplace=True)

# Guardar el archivo actualizado
df_consumo.to_csv(consumo_path, sep=';', index=False, encoding='utf-8')

print(f"Archivo actualizado con columna 'Festivo' y 'Entre semana' guardado en: {consumo_path}")


# %% [markdown]
# Empezamos a realizar el segundo modelo que constará de los precios de la energía, los datos metereologicos y, como en el dataset anterior, añadiremos las columnas Festivo y Entre semana

# %%
# Ruta de los archivos
meteorologicos_path = "Datos_limpios_meteorologicos"
precios_path = "Datos_brutos_generales/precios_energia.csv"
precios_modificado_path = "Datos_limpios_generales/precios_energia_separador_modificado.csv"
festivos_path = "Datos_brutos_generales/Festivos.csv"

# Leer los festivos
df_festivos = pd.read_csv(festivos_path, delimiter=';', encoding='utf-8')

# Estandarizar las columnas "Provincia" y "Fecha" en el dataset de festivos
df_festivos["Provincia"] = df_festivos["Provincia"].str.strip().str.upper()
df_festivos["Fecha"] = pd.to_datetime(df_festivos["Fecha"], format='%d/%m/%Y', errors='coerce')

# Modificar el delimitador del archivo de precios
df_precios = pd.read_csv(precios_path, delimiter=',', encoding='utf-8')  # Leer con coma como delimitador
df_precios.to_csv(precios_modificado_path, sep=';', index=False, encoding='utf-8')  # Guardar con punto y coma como delimitador

# Volver a cargar el archivo con el nuevo delimitador
df_precios = pd.read_csv(precios_modificado_path, delimiter=';', encoding='utf-8')

# Convertir la columna "Fecha" a formato datetime en precios
df_precios["Fecha"] = pd.to_datetime(df_precios["Fecha"], format='%Y-%m-%d', errors='coerce')

# Inicializar una lista para almacenar los DataFrames combinados
combined_dfs = []

# Procesar cada archivo en la carpeta de datos meteorológicos
for file_name in os.listdir(meteorologicos_path):
    if file_name.endswith(".csv"):  # Asegurarse de que sean archivos CSV
        file_path = os.path.join(meteorologicos_path, file_name)

        # Extraer el nombre de la provincia del archivo (sin extensión)
        provincia = os.path.splitext(file_name)[0].upper()

        # Leer el archivo meteorológico
        df_meteorologico = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

        # Convertir la columna "FECHA" a formato datetime en meteorológicos
        df_meteorologico["FECHA"] = pd.to_datetime(df_meteorologico["FECHA"], format='%Y-%m-%d', errors='coerce')

        # Añadir la columna Provincia al DataFrame meteorológico
        df_meteorologico.insert(1, "Provincia", provincia)  # Añadir la columna como segunda

        # Combinar con el archivo de precios de energía mediante la columna "Fecha"
        df_combinado = pd.merge(df_meteorologico, df_precios, left_on="FECHA", right_on="Fecha", how="left")

        # Eliminar la columna redundante "Fecha" después de la combinación
        df_combinado.drop(columns=["Fecha"], inplace=True)

        # Crear una clave de combinación basada en Fecha y Provincia para identificar festivos
        df_combinado["Clave"] = df_combinado["FECHA"].astype(str) + "_" + df_combinado["Provincia"]

        # Añadir la columna "Festivo"
        df_combinado["Festivo"] = df_combinado["Clave"].isin(
            df_festivos["Fecha"].astype(str) + "_" + df_festivos["Provincia"]
        ).map({True: "SI", False: "NO"})

        # Añadir la columna "Entre semana"
        df_combinado["Entre semana"] = df_combinado["FECHA"].dt.dayofweek.apply(lambda x: "SI" if x < 5 else "NO")

        # Eliminar la columna auxiliar "Clave"
        df_combinado.drop(columns=["Clave"], inplace=True)

        # Añadir al listado de DataFrames combinados
        combined_dfs.append(df_combinado)

# Concatenar todos los DataFrames combinados
df_final = pd.concat(combined_dfs, ignore_index=True)

# Dropear las columnas de precios que no sean necesarias
columns_to_drop = [
    "Precio medio diario sin impuestos (€/MWh)",
    "Impuesto eléctrico (€/MWh)",
    "IVA (€/MWh)"
]
df_final.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Guardar el archivo combinado
output_path = "Modelo_Precios_Met_Fest.csv"
df_final.to_csv(output_path, sep=';', index=False, encoding='utf-8')

print(f"Archivo combinado guardado en: {output_path}")

# %% [markdown]
# Debemos de rellenar todas las filas que no contengan datos, en este caso lo rellenaremos con la media de la columna (ya que el unico dataset que tiene datos faltantes es el de datos metereologicos), paorque elastic search no admite que tenga elementos faltantes.

# %%
# Lista de archivos a procesar
files = ["Modelo_Consumo_Met_fest.csv", "Modelo_Precios_Met_Fest.csv"]

# Procesar cada archivo
for file in files:
    # Leer el archivo CSV
    df = pd.read_csv(file, delimiter=';')
    
    # Eliminar filas donde todas las columnas tengan valores faltantes
    df.dropna(how='all', inplace=True)
    
    # Reemplazar valores faltantes en columnas numéricas con la media de la columna
    numeric_columns = df.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        mean_value = df[col].mean()  # Calcular la media de la columna
        df[col].fillna(mean_value, inplace=True)
    
    # Guardar el archivo procesado con un prefijo "Procesado_"
    output_file = f"{file}"
    df.to_csv(output_file, index=False, sep=';')
    print(f"Archivo procesado y guardado como: {output_file}")



