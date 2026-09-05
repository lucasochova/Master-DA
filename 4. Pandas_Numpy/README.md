# EDA y Análisis de Contratación de Depósitos Bancarios

Análisis exploratorio y temporal de una campaña de marketing bancario, con el objetivo de entender qué perfiles y qué momentos del tiempo se asocian con una mayor probabilidad de que un cliente contrate el depósito (`y`).

# EDA de Datos de Clientes

Análisis exploratorio de un dataset de clientes, con el objetivo de entender su perfil (ingreso, composición del hogar, antigüedad, comportamiento web).

## 📊 Datasets

- **Archivo:** `Datos_Limpios.csv`
- **Registros:** 42,285 clientes
- **Periodo:** 2015-01-01 a 2019-12-31
- **Variable objetivo:** `y` (`yes` / `no`) — si el cliente contrató o no el depósito

- **Archivo:** `customer-details.xlsx`
- **Registros:** 43,170 clientes (2012: 20,115 · 2013: 8,965 · 2014: 14,090)
- **Hojas:** `2012`, `2013`, `2014`

**Variables principales:**
**Archivo:** `datos_limpios.csv`
| Categoría | Columnas |
|---|---|
| Demográficas | `age`, `job`, `marital`, `education`, `grupo_edad` |
| Financieras del cliente | `default`, `housing`, `loan` |
| Campaña | `contact`, `duration`, `campaign`, `pdays`, `previous`, `poutcome` |
| Contexto económico | `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed` |
| Temporales / geográficas | `date`, `latitude`, `longitude` |

**Variables principales:**

| Categoría | Columnas |
|---|---|
| Financieras | `Income` |
| Composición del hogar | `Kidhome`, `Teenhome` |
| Comportamiento | `NumWebVisitsMonth` |
| Temporales / identificación | `Dt_Customer`, `ID` |

## 🛠️ Herramientas

- Python 3
- `pandas` / `numpy` — carga, limpieza y agregación de datos
- `matplotlib` — visualización (sin librerías de terceros para los gráficos)

## 🧹 Limpieza y preparación de datos (EDA)

Antes del análisis visual, el dataset original (`bank-additional.csv`) pasó por un proceso de exploración y limpieza (`EDA_python.ipynb`) que dio como resultado `Datos_Limpios.csv`:

1. **Exploración inicial:** revisión de tipos de datos (`info()`), estadísticas descriptivas (`describe()`), valores únicos por columna y conteo de nulos (`isnull().sum()`) para detectar inconsistencias.
2. **Tratamiento de valores nulos:**
   - `job`, `education`, `marital` → se completaron con `"abstains"` (el cliente no respondió), ya que el resto de la fila contenía datos válidos.
   - `default`, `housing`, `loan`, `euribor3m` → se completaron con `0` como valor neutral.
3. **Corrección de formato numérico:** `cons.price.idx` venía como texto con coma decimal (`,`); se reemplazó por punto (`.`) y se convirtió a numérico, eliminando las filas que no pudieron convertirse.
4. **Segmentación por edad:** se creó la columna `grupo_edad` a partir de `age`, con los rangos `0-18`, `19-30`, `31-45`, `46-60` y `60+` (los valores faltantes se etiquetaron como `"Sin dato"`).
5. **Normalización de fechas:** la columna `date` venía con el mes en español escrito con letras (ej. *"15-marzo-2017"*); se tradujo el nombre del mes a número y se convirtió a formato `datetime`, descartando las filas sin fecha válida.
6. **Verificación final:** se volvió a correr `isnull().sum()` para confirmar que no quedaran nulos relevantes antes de pasar al análisis.

## ----------------------------

1. **Carga de datos:** se leyeron las 3 hojas del Excel (`2012`, `2013`, `2014`) y se unificaron en un solo DataFrame, agregando una columna `Anio` para conservar el origen de cada fila.
2. **Limpieza de columnas:** se eliminó la columna índice residual (`Unnamed: 0`) que traía el Excel original.
3. **Exploración inicial:** revisión de tipos de datos (`info()`) y estadísticas descriptivas (`describe()`).
4. **Verificación de calidad:** conteo de nulos (`isnull().sum()`) y de IDs duplicados — el dataset no presenta nulos ni duplicados.

## 📁 Estructura del análisis

1. **Distribuciones iniciales** — edad, grupos de edad, variable objetivo (`y`), `duration`, `campaign`.
2. **Variables categóricas** — `job`, `education`, `marital`, `poutcome`.
3. **Cruces contra la variable objetivo** — grupo de edad, estado marital, tipo de contacto, duración/campaña por resultado (boxplots).
4. **Perfil de clientes que sí contrataron** — ocupación, educación y duración de llamada entre quienes dijeron `yes`.
5. **Análisis temporal** — contrataciones por mes, tasa de contratación mensual, volumen de contactos vs. tasa, comparativa anual `yes` vs `no`.
6. **Correlaciones** — mapa de calor entre variables numéricas/económicas y la contratación, como cierre del análisis.

## 🔑 Hallazgos principales

- **Tasa de contratación global:** 11.25% (4,755 de 42,285 clientes contrataron el depósito).
- **Duración de la llamada** es el factor individual más asociado a la contratación: los clientes que contrataron tuvieron llamadas de **~553 segundos en promedio**, frente a **~220 segundos** en quienes no contrataron. Es también la variable con mayor correlación positiva con `y` (0.41).
- **Edad:** los grupos extremos (**0-18 y 60+**) muestran tasas de contratación muy superiores (~44%) frente a los grupos intermedios de 31-60 años (~9-10%), aunque representan un volumen mucho menor de clientes.
- **Perfil de quienes contratan:** predominan ocupaciones *admin.* y *technician*, y niveles educativos de *university degree* y *high school*.
- **Estacionalidad:** la tasa de contratación varía a lo largo del año y entre años; el volumen de contactos no siempre coincide con los meses de mejor tasa, lo que sugiere oportunidades de enfocar campañas en los periodos de mayor conversión relativa.
- **Día de la semana:** las diferencias son leves, con el **jueves** (~12.1%) ligeramente por encima del resto de días (~11%).
- **Correlaciones con el contexto económico:** `nr.employed` (-0.36) y `pdays` (-0.33) muestran las relaciones negativas más fuertes con la contratación, sugiriendo que un mejor contexto de empleo y un mayor tiempo desde el último contacto se asocian con menor probabilidad de contratación.

## 📈 Gráficos incluidos

- Distribución de usuarios por edad y grupo de edad
- Distribución de la variable objetivo `y`
- Histogramas de `duration` y `campaign`
- Distribución de `job`, `education`, `marital`, `poutcome`
- Contratación por grupo de edad, estado marital y tipo de contacto
- Boxplots de `duration` y `campaign` según resultado
- Perfil (ocupación, educación, duración) de clientes que contrataron
- Contrataciones por mes, tasa de contratación mensual, volumen vs. tasa, comparativa anual
- Mapa de calor de correlaciones (variables numéricas/económicas vs. `y`)


## 📂 Archivos del repositorio
- `bank-additionals.csv` — datos originales
- `EDA_python.ipynb` — notebook de exploración y limpieza de datos (genera `Datos_Limpios.csv`)
- `Analisis-visual-de-datos.ipynb` — notebook con el análisis visual y temporal completoc
- `Datos_Limpios.csv` — dataset ya limpio, utilizado en el análisis
- `customer-details.xlsx` — datos originales
- `analisis_customer_details.ipynb` — notebook con la carga, exploración inicial y primeras visualizaciones
- `README.md` — este documento
