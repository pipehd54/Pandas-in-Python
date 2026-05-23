# Pandas in Python

A collection of Python scripts for practicing data manipulation and analysis with [Pandas](https://pandas.pydata.org/).

## Contents

| Script | Description |
|--------|-------------|
| `scripts/contactos.py` | DataFrame creation, filtering, grouping, and classification from a contacts dataset |
| `scripts/analisis_ventas.py` | Multi-table merge analysis (ventas, productos, tiendas) with aggregations |
| `scripts/ventas_pescador.py` | Sales data exploration — basic stats, filtering, and computed columns |
| `scripts/app_moviles.py` | DataFrame inspection methods (`head`, `info`, `describe`, `shape`) and column operations |
| `guides/guia_panda.py` | Step-by-step pandas reference covering creation, filtering, grouping, merging, and export |

## Requirements

- Python 3.9+
- pandas
- matplotlib
- openpyxl (for Excel export)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Navigate to the project root and run any script:

```bash
python scripts/contactos.py
python scripts/analisis_ventas.py
```

## Project Structure

```
Pandas-in-Python/
├── data/          # Source CSV datasets
├── scripts/       # Data analysis scripts
├── guides/        # Learning resources and tutorials
├── requirements.txt
├── LICENSE
└── README.md
```

## License

MIT
