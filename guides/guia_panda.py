import pandas as pd

# Formas de crear un DataFrame desde cero:

# Diccionario:
data = {
    "ciudad": ["Cali", "Medellin", "Bogota", "Barranquilla", "Virginia", "Mexico City", "Lima"],
    "pais": ["Colombia", "Colombia", "Colombia", "Colombia", "Estados Unidos", "Mexico", "Peru"],
    "poblacion": [2400000, 2500000, 8000000, 1200000, 1500000, 9000000, 8000000]
}

df = pd.DataFrame(data)
print(df)

print("\n")

# Lista de listas:
adata = [
    ["Cali", "Colombia", 2400000],
    ["Medellin", "Colombia", 2500000],
    ["Bogota", "Colombia", 8000000],
    ["Barranquilla", "Colombia", 1200000],
    ["Virginia", "Estados Unidos", 1500000],
    ["Mexico City", "Mexico", 9000000],
    ["Lima", "Peru", 8000000]
]
df2 = pd.DataFrame(adata, columns=["ciudad", "pais", "poblacion"])
print(df2)

# Importar desde un archivo CSV o Excel: 
# df = pd.read_csv("nombre_archivo.csv")
# df = pd.read_excel("nombre_archivo.xlsx")

# Inspeccion rapida (Tambien se puede con print), sirve para revisar que datos hay:
df.head() # Primeras filas
df.tail() # Ultimas filas
df.shape # (Filas, Columnas)
df.info() # Tipos de datos y nulos
df.describe() # Estadisticas de columnas numericas
df.columns # Nombres de columnas
df.index # Rango de indices
df.dtypes # Tipos de datos

print("\n")

# Seleccion de datos, sirve para trabajar con columnas o filas especificas:
df["ciudad"] # Selecciona una columna
df[["ciudad", "poblacion"]] # Selecciona multiples columnas
df.iloc[0] # Selecciona la primera fila 
df.loc[0, "poblacion"] # Primera fila, columna especifica

print("\n")

# Filtrado por condicion:
print(df[df["poblacion"] > 2000000]) # Filtra filas con poblacion mayor a 2 millones
print(df[(df["ciudad"] == "Cali") & (df["poblacion"] > 2000000)]) # Filtra filas con ciudad Cali y poblacion mayor a 2 millones

print("\n")

# Modificar Columnas: 
df["total"] = df["poblacion"] * df["poblacion"] # Crea una nueva columna con el cuadrado de la poblacion
# print(df)
df.rename(columns={"poblacion": "poblacion_ciudad"}, inplace=True) # Renombra una columna
# print(df)
df.drop(columns=["total"], inplace=True) # Elimina una columna
print(df)

print("\n")

# Ordenar datos, sirve para ver los registros mas grandes o mas pequeños:
df_orden = df.sort_values(by="poblacion_ciudad", ascending=False) # Ordena por poblacion de mayor a menor
print(df_orden)
df_desorden = df.sort_values(["poblacion_ciudad", "ciudad"], ascending=[False, True]) # Ordena por poblacion de mayor a menor y luego por ciudad de A a Z
print(df_desorden)

print("\n")

# Valores nulos, en datos reales hay valores faltantes, y necesitas decidir que hacer con ellos:
df.isnull().sum() # Cuenta los valores nulos por columna
df.dropna() # Eliminar filas con nulos
df.fillna(0) # Rellanar datos nulos con 0
df.fillna({"poblacion_ciudad": df["poblacion_ciudad"].mean()})

print("\n")

# Agrupaciones (groupby), sirve para resumir datos, como en tablas dinamicas de Excel:
dfl = df.groupby("ciudad")["poblacion_ciudad"].mean() # Agrupa por ciudad y calcula la media de poblacion_ciudad
# print(dfl)
df3 = df.groupby("ciudad")["poblacion_ciudad"].sum() # Agrupa por ciudad y calcula la suma de poblacion_ciudad
# print(df3)
df4 = df.groupby("pais").agg({
    "poblacion_ciudad": "mean",
    "ciudad": "sum"
})

print(df4) # Agrupa por pais y calcula la media de poblacion_ciudad y la suma de ciudades aunque mayormente son deben ser numeros

print("\n")

# Combinar tablas (merge y concat), sirve para unir diferentes DataSets:
# ventas = pd.read_csv("nombre_archivo_csv")
# productos = pd.read_csv("nombre_archivo_csv")
# df = pd.merge(ventas, productos, on="id_producto")
# Concatenar (apilar):
# df_total = pd.concat([df1, df2], axis=0) # Filas
# df_total = pd.concat([df1, df2], axis=1) # Columnas

print("\n")

# Estadisticas rapidas, para obtener conteos y valores mas comunes:
lol = df["ciudad"].value_counts() # Cuenta los valores unicos de la columna ciudad
print(lol)
lol1 = df["ciudad"].mode()[0] # Valor mas frecuente
print(lol1)
lol2 = df["poblacion_ciudad"].max(), df["ciudad"].min() # Maximo y minimo
print(lol2)

print("\n")

# Exportar resultados
df.to_csv("resultado.csv", index=False) # Exporta a CSV
df.to_excel("resultado.xlsx", index=False) # Exporta a Excel








