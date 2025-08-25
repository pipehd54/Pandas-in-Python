import pandas as pd

df = pd.read_csv("contactos_actualizados.csv")
print(df.head()) # Muestra las primeras 5 filas
print("\n") # Si se desea mostrar mas hay que agregar el numero que desee dentro de ()
print(df.tail()) # Muestra las ultimas 5 filas
print("\nMuestra metadatos clave del DataFrame .info(): ")
print(df.info())
print("\nGenera estadisticas descriptivas para columas numericas .describe(): ")
print(df.describe(include="all"))
print("\nPara ver informacion de una columna es df[nombre de la columna: ")
print(df["pais"])
print("\nPara ver informacion de varias columnas: ")
solo_nombre_y_edad = df[["nombre", "edad"]]
print(solo_nombre_y_edad)
print("\n") # Acceder a todas las columas exepto una con .drop()
removed_nombre_df = df.drop("nombre", axis=1)
print(removed_nombre_df)
print("\n") # Muestra el numero de columnas y filas con .shape
print(df.shape)
print("\n") # Muestra como esta organizada la informacion en codigo con .values
print(df.values)
print("\n") # Muestra solo las columnas con .columns
print(df.columns)
print(df.index)
print("\n") # Ordena las columnas con .sort_values y con ascending=False (mayor a menor)
print(df.sort_values(["edad", "numero"], ascending=[True, False]))
print("\n") # Para mostrar las columnas
print(df[["nombre", "pais"]])

print("\nFiltros con condiciones: ")
print(df[df["edad"] > 25])
print("\n")
print(df[(df["pais"] == "Colombia") & (df["edad"] < 30)])

print("\nCreacion y modificacion de columnas: ")
df["mayor_de_edad"] = df["edad"] > 18
df.rename(columns={"numero": "telefono"}, inplace=True)
print(df)

print("\nValores nulos: ")
df = df.fillna({"edad": df["edad"].mean()})
print(df)

print("\nAgrupacion con groupby: ")
print(df.groupby("pais")["edad"].mean())
print(df.groupby("pais").agg({"edad": "mean", "telefono": "count"}))

print("\nExportar resultados: ")
df.to_csv("resultado.csv", index=False)