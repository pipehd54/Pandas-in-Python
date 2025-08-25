import pandas as pd
import matplotlib.pyplot as plt

contacts = [
    ["Andres", "Colombia", "Hijo", 20, 3194971221],
    ["Carolina", "USA", "Amiga", 16, 1234567895],
    ["Miguel", "Colombia", "Amigo", 21, 9876543217],
    ["Rita", "Mexico", "Amiga", 23, 1478523690],
    ["Saul", "Colombia", "Padre", 55, 3214597567],
    ["Ofelia", "Colombia", "Madre", 49, 7891234546]
]

df = pd.DataFrame(contacts, columns=["nombre", "pais", "rol", "edad", "numero"])
df["es_familia"] = df["rol"].isin(["Padre", "Madre", "Hijo"])
print(df)

print("\nFiltros basicos: ")
# Mayores de 18 años
mayores = df[df["edad"] > 18]
print(mayores)
# Contactos de Colombia
print("\n")
colombianos = df[df["pais"] == "Colombia"]
print(colombianos)

print("\nAgrupaciones y Estadisticas: ")
# Promedio de edad por pais
print(df.groupby("pais")["edad"].mean())
print("\n")
# Cantidad de contactos por rol
print(df["rol"].value_counts())

print("\nClasificacion generacional: ")
df["generacion"] = df["edad"].apply(lambda x: "Gen Z" if x < 25 else "Millenial" if x > 40 else "Boomer")
print(df)

print("\nOrdenamiento: ")
# Ordenar por edad
print(df.sort_values("edad", ascending=False))

print("\nExportar/Importar datos: ")
# Guardar como CSV
df.to_csv("contactos_actualizados.csv", index=False)
print("\n")
# Leer el archivo guardado
nuevo_df = pd.read_csv("contactos_actualizados.csv")
print(nuevo_df)


df.plot(kind="bar", x="nombre", y="edad", legend=False)
plt.title("Edad de contactos")
plt.show()