import pandas as pd
import matplotlib.pyplot as plt


def main():
    df_ventas = pd.read_csv("data/ventas.csv")
    df_productos = pd.read_csv("data/productos.csv")
    df_tiendas = pd.read_csv("data/tiendas.csv")

    print("\nVentas: ")
    print(df_ventas.info())
    print("\nProductos: ")
    print(df_productos.head(3))
    print("\nTiendas: ")
    print(df_tiendas["ciudad"].value_counts())

    df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"])
    df_ventas["margen"] = df_ventas["total"] * 0.4
    print(df_ventas)

    top_categorias = df_ventas.groupby("id_producto")["total"].sum().sort_values(ascending=False)
    print(top_categorias)
    top_categorias.plot(kind="bar", title="Ventas totales")
    plt.show()


if __name__ == "__main__":
    main()
