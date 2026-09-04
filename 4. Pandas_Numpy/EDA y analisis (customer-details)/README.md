# EDA de Datos de Clientes

Análisis exploratorio de un dataset de clientes, con el objetivo de entender su perfil (ingreso, composición del hogar, antigüedad, comportamiento web).

## 📊 Dataset

- **Archivo:** `customer-details.xlsx`
- **Registros:** 43,170 clientes (2012: 20,115 · 2013: 8,965 · 2014: 14,090)
- **Hojas:** `2012`, `2013`, `2014`
- **Variable objetivo:** _Pendiente de definir_

**Variables principales:**

| Categoría | Columnas |
|---|---|
| Financieras | `Income` |
| Composición del hogar | `Kidhome`, `Teenhome` |
| Comportamiento | `NumWebVisitsMonth` |
| Temporales / identificación | `Dt_Customer`, `ID` |

## 🛠️ Herramientas

- Python 3
- `pandas` — carga, unión y exploración de datos
- `matplotlib` — visualización

## 🧹 Limpieza y preparación de datos (EDA)

Primeros pasos realizados sobre el archivo original (`customer-details.xlsx`), en el notebook `analisis_customer_details.ipynb`:

1. **Carga de datos:** se leyeron las 3 hojas del Excel (`2012`, `2013`, `2014`) y se unificaron en un solo DataFrame, agregando una columna `Anio` para conservar el origen de cada fila.
2. **Limpieza de columnas:** se eliminó la columna índice residual (`Unnamed: 0`) que traía el Excel original.
3. **Exploración inicial:** revisión de tipos de datos (`info()`) y estadísticas descriptivas (`describe()`).
4. **Verificación de calidad:** conteo de nulos (`isnull().sum()`) y de IDs duplicados — el dataset no presenta nulos ni duplicados.

_Pendiente: tratamiento de outliers, normalización de fechas (`Dt_Customer`), y cualquier transformación adicional según la pregunta de negocio que se defina._

## 📁 Estructura del análisis

1. **Distribuciones iniciales** — ingreso (`Income`).
2. **Comparativas por año** — cantidad de clientes por hoja/año.
3. **Relación entre variables** — ingreso vs. visitas web mensuales.
4. _Pendiente: cruces contra composición del hogar (`Kidhome`, `Teenhome`), análisis de antigüedad a partir de `Dt_Customer`, segmentación de clientes, correlaciones._

## 🔑 Hallazgos principales

_Pendiente — a completar a medida que avance el análisis._

## 📈 Gráficos incluidos

- Histograma de distribución de `Income`
- Cantidad de clientes por año (hoja de origen)
- Scatter de `Income` vs. `NumWebVisitsMonth`

_Pendiente: gráficos adicionales según los próximos pasos del análisis._

## 📂 Archivos del repositorio

- `customer-details.xlsx` — datos originales
- `analisis_customer_details.ipynb` — notebook con la carga, exploración inicial y primeras visualizaciones
- `README.md` — este documento
