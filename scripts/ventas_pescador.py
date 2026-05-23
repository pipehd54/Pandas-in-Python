import pandas as pd


def main():
    df = pd.read_csv("data/ventas.csv")

    print("\nPrimeras filas: ")
    print(df.head())

    print("\nResumen estadistico: ")
    print(df.describe())

    print("\nProductos con cantidad > 5: ")
    print(df[df["Cantidad"] > 5])

    print("\nCalcular el total de ventas por producto: ")
    df["Total_Ventas"] = df["Cantidad"] * df["Precio_Unitario"]
    ventas_por_producto = df.groupby("Producto")["Total_Ventas"].sum()
    print(ventas_por_producto)

    print("\nGuardar DataFrame modificado en un nuevo CSV: ")
    df.to_csv("ventas_actualizadas.csv", index=False)


if __name__ == "__main__":
    main()
