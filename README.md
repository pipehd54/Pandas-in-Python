# Pandas in Python

A collection of Python scripts for practicing data manipulation and analysis with [Pandas](https://pandas.pydata.org/).

---

## Contents / Contenido

| Script | Description / Descripción |
|--------|--------------------------|
| `scripts/contactos.py` | DataFrame creation, filtering, grouping, and classification from a contacts dataset / Creación, filtrado, agrupación y clasificación de un DataFrame a partir de contactos |
| `scripts/analisis_ventas.py` | Multi-table merge analysis (ventas, productos, tiendas) with aggregations / Análisis con fusión de múltiples tablas (ventas, productos, tiendas) y agregaciones |
| `scripts/ventas_pescador.py` | Sales data exploration — basic stats, filtering, and computed columns / Exploración de ventas — estadísticas básicas, filtros y columnas calculadas |
| `scripts/app_moviles.py` | DataFrame inspection methods (`head`, `info`, `describe`, `shape`) and column operations / Métodos de inspección de DataFrames y operaciones con columnas |
| `guides/guia_panda.py` | Step-by-step pandas reference covering creation, filtering, grouping, merging, and export / Guía paso a paso de pandas: creación, filtrado, agrupación, fusión y exportación |

## Requirements / Requisitos

- Python 3.9+
- pandas
- matplotlib
- openpyxl (for Excel export / para exportar a Excel)

Install dependencies / Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Usage / Uso

Navigate to the project root and run any script /
Navega a la raíz del proyecto y ejecuta cualquier script:

```bash
python scripts/contactos.py
python scripts/analisis_ventas.py
```

## Project Structure / Estructura del proyecto

```
Pandas-in-Python/
├── data/          # Source CSV datasets / Datos fuente en CSV
├── scripts/       # Data analysis scripts / Scripts de análisis
├── guides/        # Learning resources and tutorials / Guías y tutoriales
├── requirements.txt
├── LICENSE
└── README.md
```

## License / Licencia

MIT
