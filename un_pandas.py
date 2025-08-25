import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.read_csv("ventas.csv")
df_productos = pd.read_csv("productos.csv")
df_tiendas = pd.read_csv("tiendas.csv")

print("\nVentas: ")
print(df_ventas.info()) # Ver estructuras y tipos de datos
print("\nProductos: ")
print(df_productos.head(3)) # Primeras filas
print("\nTiendas: ")
print(df_tiendas["ciudad"].value_counts()) # Conteo por ciudad

df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"])
df_ventas["margen"] = df_ventas["total"] * 0.4
print(df_ventas)

top_categorias = df_ventas.groupby("id_producto")["total"].sum().sort_values(ascending=False)
print(top_categorias)
top_categorias.plot(kind="bar", title="Ventas totales")
plt.show()