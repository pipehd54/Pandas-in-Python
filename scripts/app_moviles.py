import pandas as pd


def main():
    df = pd.read_csv("contactos_actualizados.csv")
    print(df.head())
    print("\n")
    print(df.tail())
    print("\nMuestra metadatos clave del DataFrame .info(): ")
    print(df.info())
    print("\nGenera estadisticas descriptivas para columas numericas .describe(): ")
    print(df.describe(include="all"))
    print("\nPara ver informacion de una columna es df[nombre de la columna: ")
    print(df["pais"])
    print("\nPara ver informacion de varias columnas: ")
    solo_nombre_y_edad = df[["nombre", "edad"]]
    print(solo_nombre_y_edad)
    print("\n")
    removed_nombre_df = df.drop("nombre", axis=1)
    print(removed_nombre_df)
    print("\n")
    print(df.shape)
    print("\n")
    print(df.values)
    print("\n")
    print(df.columns)
    print(df.index)
    print("\n")
    print(df.sort_values(["edad", "numero"], ascending=[True, False]))
    print("\n")
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


if __name__ == "__main__":
    main()
