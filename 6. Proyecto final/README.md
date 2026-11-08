# 6. Proyecto final: Felicidad mundial 2015-2019

Análisis de los datos del **World Happiness Report** entre 2015 y 2019, con el objetivo de **mostrar los datos y las relaciones entre sus variables de la forma más clara posible**. El proyecto recorre el ciclo completo: datos crudos → limpieza y unificación en Python (ETL) → informe interactivo en Power BI.

## 📖 Descripción

Cada año el informe publica una puntuación de felicidad por país (*Score*) junto con seis factores que contribuyen a ella: PIB, apoyo social, esperanza de vida, libertad, ausencia de corrupción y generosidad. Los cinco ficheros anuales no usan los mismos nombres de columna ni las mismas columnas, así que el primer paso es unificarlos en una única tabla. Sobre esa tabla se construye un informe de Power BI con un **segmentador de año** que permite analizar cada variable año a año y, después, sus relaciones en conjunto.

## 🗂️ Estructura de la carpeta

```
6. Proyecto final/
├── 0. Datos crudos/
│   ├── Happines-country/        # Datos usados: informes de 2015 a 2019 (CSV)
│   ├── CO2/                     # Emisiones de CO2 (no se usa en este análisis)
│   └── E-Comerce/               # Datos de comercio electrónico (no se usa en este análisis)
├── 1. ETL/
│   ├── ETL.ipynb                # Notebook de limpieza y unificación
│   ├── 2015.csv … 2019.csv      # Copias de los ficheros anuales con los que trabaja el notebook
│   └── Datos_Limpios15-19.csv   # Resultado del ETL: tabla única que consume Power BI
├── 2.Analisis/
│   ├── Proyecto_Final.pbix      # Informe de Power BI
│   └── Tema_Terroso.json        # Tema de colores (opcional)
└── README.md
```

## 🔄 Pasos del proyecto

### 1. Datos crudos
Se parte de cinco ficheros CSV, uno por año (2015-2019), con entre 155 y 158 países cada uno. Los nombres de columna cambian de un año a otro (por ejemplo `Happiness Score`, `Happiness.Score` y `Score`), y algunas columnas solo existen en ciertos años.

### 2. ETL con Python (`1. ETL/ETL.ipynb`)
1. Importar los cinco ficheros con **pandas**.
2. Añadir la columna `AÑO` a cada uno para poder identificar las filas tras la unión.
3. Revisar las columnas de cada año.
4. Unificar los nombres con un diccionario de equivalencias (`Happiness Rank` / `Overall rank` → `Rank`, `Economy (GDP per Capita)` → `GDP`, `Family` → `Social support`, `Trust (Government Corruption)` / `Perceptions of corruption` → `Corruption`, etc.).
5. Concatenar los cinco años conservando **solo las columnas comunes a todos** (las que no existen en los cinco años, como `Region`, `Standard Error` o `Dystopia Residual`, se descartan).
6. Verificar el resultado: 782 filas, filas por año y valores nulos.
7. Exportar `Datos_Limpios15-19.csv` (separador coma, codificación `utf-8-sig`).

**Resultado: 782 filas, 170 países distintos (141 con datos en los cinco años) y 10 columnas:**

| Columna | Descripción |
|---|---|
| `Country` | País |
| `Rank` | Posición en el ranking del año (1 = mayor puntuación) |
| `Score` | Puntuación de felicidad (en estos datos, entre 2,69 y 7,77) |
| `GDP` | Contribución del PIB per cápita a la puntuación |
| `Social support` | Contribución del apoyo social (en 2015-2017 la columna original se llamaba `Family`) |
| `Life expectancy` | Contribución de la esperanza de vida saludable |
| `Freedom` | Contribución de la libertad para tomar decisiones de vida |
| `Corruption` | Contribución de la percepción de corrupción: un valor alto significa **menos** corrupción percibida |
| `Generosity` | Contribución de la generosidad |
| `AÑO` | Año del informe (2015-2019) |

Hay un único valor nulo: `Corruption` de Emiratos Árabes Unidos en 2018.

### 3. Análisis en Power BI (`2.Analisis/Proyecto_Final.pbix`)
El informe tiene **8 hojas** y comparte el segmentador de año entre ellas (se mantiene la selección al cambiar de hoja):

| Hoja | Qué muestra |
|---|---|
| Resumen y evolución | Tarjetas con la media de cada variable, top 10 de países por puntuación, media de cada variable en el año elegido y evolución 2015-2019. Incluye una guía de lectura. |
| Variables por año | Para cada variable: reparto entre los países del año elegido y máximo, media y mínimo de cada año. |
| Análisis conjunto | Seis dispersiones de la puntuación frente a cada variable, con línea de tendencia y su correlación. |
| Correlaciones | Correlación de cada variable con la puntuación en el año elegido, su evolución por año y una tabla resumen. |
| Mapa y ranking | Mapa con el ranking de todos los países y top 15 del año elegido. |
| Comparador de países | Selección de países para comparar su ranking, su puntuación y cada variable a lo largo de los años. |
| Cambios 2015-2019 | Los 10 países que más suben y los 10 que más bajan entre 2015 y 2019. |
| Conclusiones | Resumen de los hallazgos. |

Los gráficos marcados como «todos los años» ignoran el segmentador a propósito, porque su función es comparar los cinco años.

**Medidas DAX** (10): `Score medio`, `Score año anterior`, `Variación vs año anterior`, seis medidas de **correlación de Pearson** con la puntuación (una por variable, calculadas sobre los países del año seleccionado) y `Cambio Score 2015-2019`.

**Paleta de colores:** tonos amarillos, marrones y terrosos, con colores distintos para cada variable y los mismos en todas las hojas. El fichero `Tema_Terroso.json` contiene la paleta como tema de Power BI (Vista → Temas → Examinar temas).

## 🔎 Principales resultados

| Año | Países | Puntuación media | Desv. típica |
|---|---|---|---|
| 2015 | 158 | 5,38 | 1,15 |
| 2016 | 157 | 5,38 | 1,14 |
| 2017 | 155 | 5,35 | 1,13 |
| 2018 | 156 | 5,38 | 1,12 |
| 2019 | 156 | 5,41 | 1,11 |

- **El promedio mundial apenas cambia** y la dispersión entre países se mantiene estable.
- **El podio y el último puesto sí cambian de nombres:** en 2015 lideraban Suiza, Islandia y Dinamarca y en 2019 Finlandia, Dinamarca y Noruega. Por abajo, Togo, Burundi y Siria (2015) dan paso a Sudán del Sur, República Centroafricana y Afganistán (2019).
- **PIB, apoyo social y esperanza de vida** son las variables más relacionadas con la puntuación (correlaciones entre 0,72 y 0,81 en todos los años). Libertad (en torno a 0,55) y ausencia de corrupción (en torno a 0,40) pesan menos.
- **La generosidad apenas discrimina:** su correlación baja de 0,18 en 2015 a 0,08 en 2019.
- **Mayores cambios entre 2015 y 2019** (149 países con dato en ambos años): Venezuela es el que más cae (-2,10 puntos) y Benín el que más sube (+1,54), seguido de Costa de Marfil (+1,29) y Togo (+1,25).

## ⚠️ Limitaciones y decisiones a tener en cuenta

- **Las variables no son unidades reales:** son contribuciones estimadas a la puntuación. Por eso `Corruption` se muestra como «ausencia de corrupción» (valor alto = menos corrupción percibida).
- **Posibles cambios de definición entre años:** el apoyo social pasa de una media de 0,79 en 2016 a 1,19 en 2017 y la esperanza de vida sube en 2019 (0,73 frente a 0,55-0,63 en años anteriores). Los saltos parecen metodológicos, no reales; conviene comparar tendencias con cautela. Las correlaciones dentro de un mismo año no se ven afectadas.
- **Panel no equilibrado:** no todos los países aparecen todos los años (170 distintos, 141 en los cinco años). Los cambios 2015-2019 usan solo los que tienen ambos años.
- **Sin región:** al conservar solo las columnas comunes a los cinco años se pierde `Region`, así que no hay análisis por regiones.
- **Correlación no implica causalidad.** `Rank` es redundante con `Score` y no se usa para correlaciones.
- **Tipos de datos en Power BI:** las columnas numéricas con decimales (`Score`, `GDP`, etc.) deben importarse como *número decimal* con configuración regional **Inglés (EE. UU.)**. Con configuración española, Power BI interpreta el punto decimal como separador de miles y los valores se multiplican por 1.000 o más.

## 🛠️ Requisitos y cómo reproducirlo

- Python 3.x con `pandas`, `numpy` y `jupyter` (`pip install pandas numpy jupyter`)
- Power BI Desktop (para abrir el `.pbix`)

1. Abre `1. ETL/ETL.ipynb` y ejecútalo para regenerar `Datos_Limpios15-19.csv` a partir de los CSV anuales.
2. Abre `2.Analisis/Proyecto_Final.pbix` en Power BI Desktop. El informe apunta a la ruta local donde se desarrolló; si no encuentra el CSV, ve a *Inicio → Transformar datos → Configuración de origen de datos → Cambiar origen* y selecciona `1. ETL/Datos_Limpios15-19.csv`.
3. Pulsa *Actualizar* para cargar los datos.

## ✒️ Autor

- Lucas Ochova
- [@lucasochova](https://github.com/lucasochova)

## Para la resolucion del proyecto se utilizo la herramienta de IA Claude, quien aporto sugerencias, creo el tema de colores, acorde a lo solicitado, e impulso las ideas creativas que se tenian para el proyecto, asi como aporto calculos avanzados de DAX, que permitieron dar mayor alcance al informe.  