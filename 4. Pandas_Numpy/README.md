# 4. Pandas_Numpy — EDA y Análisis de Contratación de Depósitos Bancarios

Análisis exploratorio y de relación entre el perfil de clientes y la contratación de un depósito bancario (`y`),
combinando dos fuentes de datos: una campaña de marketing bancario y un dataset de detalle de clientes.

## 📊 Datasets

**`bank-additional.csv` → `Datos_Limpios.csv`**
- **Registros:** 42,285 clientes
- **Periodo:** 2015-01-01 a 2019-12-31
- **Variable objetivo:** `y` (`yes` / `no`) — si el cliente contrató o no el depósito

**`customer-details.xlsx`**
- **Registros:** 43,170 clientes (2012: 20,115 · 2013: 8,965 · 2014: 14,090)
- **Hojas:** `2012`, `2013`, `2014`

**Clave de unión:** `ID` (customer-details) / `id_` (Datos_Limpios) — coincide exactamente para 42,285 clientes.

**Variables principales:**

| Categoría | Columnas |
|---|---|
| Demográficas | `age`, `job`, `marital`, `education`, `grupo_edad` |
| Financieras del cliente | `default`, `housing`, `loan`, `Income` |
| Composición del hogar | `Kidhome`, `Teenhome` |
| Campaña | `contact`, `duration`, `campaign`, `pdays`, `previous`, `poutcome` |
| Contexto económico | `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed` |
| Temporales / geográficas | `date`, `Dt_Customer`, `latitude`, `longitude` |
| Comportamiento web | `NumWebVisitsMonth` |

## 🛠️ Herramientas

- Python 3
- `pandas` / `numpy` — carga, limpieza, fusión y agregación de datos
- `matplotlib` — visualización (sin librerías de terceros para los gráficos)

## 🧹 Limpieza y preparación de datos (ETL)

**Campaña bancaria** (`00. ETL_bank-additionals.ipynb`, sobre `bank-additional.csv`):
1. Exploración inicial: tipos de datos, estadísticas descriptivas, nulos por columna.
2. Nulos en `job`, `education`, `marital` → completados como `"abstains"`; `default`, `housing`, `loan`,
   `euribor3m` → completados con `0`.
3. `cons.price.idx` venía como texto con coma decimal → convertido a numérico.
4. Creación de `grupo_edad` a partir de `age` (`0-18`, `19-30`, `31-45`, `46-60`, `60+`).
5. Normalización de `date` (mes en español escrito con letras → `datetime`).
6. Verificación final de nulos → resultado: `Datos_Limpios.csv`.

**Detalle de clientes** (`02. ETL-EDA_customer_details.ipynb`, sobre `customer-details.xlsx`):
1. Carga de las 3 hojas (`2012`, `2013`, `2014`) y unificación en un solo DataFrame con columna `Anio`.
2. Eliminación de la columna índice residual del Excel.
3. Verificación de calidad: sin nulos ni IDs duplicados.

## 📁 Estructura del análisis

1. **`00. ETL_bank-additionals.ipynb`** — limpieza de la campaña bancaria.
2. **`01. EDA_bank-additionals.ipynb`** — distribuciones iniciales, variables categóricas, cruces contra `y`
   (grupo de edad, estado marital, tipo de contacto, duración/campaña), perfil de clientes que contrataron,
   análisis temporal (mensual y anual) y correlaciones.
3. **`02. ETL-EDA_customer_details.ipynb`** — carga y limpieza de `customer-details`, distribución de `Income`,
   clientes por año, y cruces de `Kidhome`/`Teenhome` contra `Income` y `NumWebVisitsMonth` (boxplots, mapa de
   correlación, antigüedad del cliente).
4. **`03. Analisis_Fusion_y.ipynb`** — fusión de ambos datasets por `ID`/`id_`, y relación de `y` con
   `Kidhome`/`Teenhome`, `Income` y antigüedad del cliente (`Dt_Customer`), con una comparación adicional del
   grupo de menor antigüedad (historial de contactos previos y tipo de contacto).

## 🔑 Hallazgos principales

**Campaña bancaria:**
- **Tasa de contratación global:** 11.25% (4,755 de 42,285 clientes).
- **`duration`** es la variable individual más asociada a `y`: ~553s de promedio en quienes contrataron vs.
  ~220s en quienes no (correlación 0.41).
- **Edad:** los grupos extremos (0-18 y 60+) muestran tasas de contratación mucho más altas (~44%) que los
  grupos intermedios (~9-10%), aunque con mucho menor volumen de clientes.
- **Estacionalidad:** la tasa de contratación varía por mes y por año; el volumen de contactos no siempre
  coincide con los meses de mejor tasa.
- **Contexto económico:** `nr.employed` (-0.36) y `pdays` (-0.33) son las correlaciones negativas más fuertes
  con `y`.

**Detalle de clientes (`customer-details`):**
- `Income`, `Kidhome`, `Teenhome` y `NumWebVisitsMonth` muestran una distribución muy uniforme entre sí — sin
  relaciones relevantes (boxplots y correlaciones cercanas a 0).

**Fusión de ambos datasets:**
- `Kidhome`, `Teenhome` e `Income` **no muestran relación** con `y` (tasas de contratación prácticamente
  iguales entre grupos, ~11% en todos los casos).
- La **antigüedad del cliente** (`Dt_Customer`) sí muestra una diferencia marcada: los clientes con
  antigüedad ≤ 400 días contratan a una tasa de ~22%, frente a ~5-7% en el resto.
- Esa diferencia **no se explica por perfil demográfico**, sino por historial de campaña: el grupo de menor
  antigüedad tiene muchos más contactos previos (`previous` promedio 0.44 vs. 0.04) y fue contactado
  mayoritariamente por celular (86.7% vs. 51.5%). Es decir, la antigüedad actúa como un proxy de "cliente ya
  contactado en campañas anteriores", no como una variable independiente.

## 📈 Gráficos incluidos

Ver carpeta `Graficos/` (19 imágenes numeradas según el orden del análisis de la campaña bancaria):
distribuciones iniciales, variables categóricas, cruces contra `y`, perfil de clientes que contrataron,
análisis temporal y mapa de correlaciones. Los gráficos del análisis de `customer-details` y de la fusión
quedan embebidos directamente en sus respectivos notebooks (`02` y `03`).

## 📂 Archivos del repositorio

- `bank-additional.csv` — datos originales de la campaña bancaria
- `customer-details.xlsx` — datos originales de clientes
- `Datos_Limpios.csv` — campaña bancaria ya limpia (salida de `00`)
- `00. ETL_bank-additionals.ipynb` — limpieza de la campaña bancaria
- `01. EDA_bank-additionals.ipynb` — análisis exploratorio y temporal de la campaña
- `02. ETL-EDA_customer_details.ipynb` — carga, limpieza y exploración de clientes
- `03. Analisis_Fusion_y.ipynb` — fusión de datasets y análisis de `y` vs. perfil de cliente
- `Graficos/` — imágenes generadas durante el EDA de la campaña bancaria
- `datos originales/` — copia de los datos crudos y el enunciado del proyecto
- `README.md` — este documento
