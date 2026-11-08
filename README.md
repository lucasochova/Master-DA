# 🎓 Master-DA: Proyectos del Máster en Análisis de Datos

Repositorio con los proyectos y ejercicios realizados a lo largo del Máster en Análisis de Datos. Incluye trabajos de dashboarding, SQL, Python, análisis de datos con Pandas/Numpy, Business Intelligence con Power BI y un proyecto final de principio a fin (ETL + análisis).

## 📖 Descripción

Este repositorio recopila los distintos proyectos y ejercicios entregados en cada módulo del máster. El objetivo es documentar el progreso y las técnicas aprendidas: desde la creación de dashboards y consultas SQL, hasta el análisis de datos con Python, Pandas y Numpy, la visualización con Power BI y un proyecto final que integra todo el ciclo de trabajo con datos.

## 🗂️ Estructura del Proyecto

```
Master-DA/
├── 1. primer proyecto dashboard/   # Dashboard de ventas de videojuegos
│   └── Dataset/                    # Datos crudos y procesados (CSV)
├── 2. SQL/                         # Ejercicios SQL sobre la base de datos Sakila
├── 3. Python/                      # Katas de Python (ejercicios de práctica)
├── 4. Pandas_Numpy/                # Proyecto EDA con Pandas y Numpy
│   └── (notebook, datos de clientes y de campaña bancaria)
├── 5. PowerBI/                     # Proyectos de Business Intelligence en Power BI
│   └── datos proyecto 2/           # Datos de clientes, productos, pedidos y vendedores
├── 6. Proyecto final/              # Felicidad mundial 2015-2019: ETL en Python + informe en Power BI
│   ├── 0. Datos crudos/            # Datos de partida (informes anuales de felicidad y otros datasets)
│   ├── 1. ETL/                     # Notebook de limpieza y tabla unificada (CSV)
│   └── 2.Analisis/                 # Informe de Power BI y tema de colores
└── README.md
```

## 🛠️ Instalación y Requisitos

Este proyecto usa **Python 3.x** y, según el módulo, requiere:

- pandas
- numpy
- jupyter
- Excel (para abrir los archivos `.xlsx`)
- MySQL o similar (para ejecutar las consultas de la base de datos Sakila)
- Power BI Desktop (para abrir los archivos `.pbix`)

Instalación rápida de las dependencias de Python:

```bash
pip install pandas numpy jupyter
```

## 📊 Proyectos incluidos

### 1️⃣ Primer Proyecto: Dashboard de Ventas de Videojuegos
Análisis y creación de un dashboard en Excel a partir del dataset "Video Games Sales (1980-2024)". Incluye limpieza de datos y visualización de tendencias de ventas por plataforma, género y región.

### 2️⃣ SQL: Base de Datos Sakila
Ejercicios de consultas SQL sobre el esquema de alquiler de películas Sakila (filtrado, joins, funciones de agregación). Incluye el diagrama entidad-relación de la base de datos.

### 3️⃣ Python: Katas
Serie de ejercicios ("katas") de práctica en Python para reforzar lógica de programación, estructuras de datos y buenas prácticas de código, disponibles tanto en `.py` como en `.ipynb`.

### 4️⃣ Pandas & Numpy: EDA con Python
Análisis exploratorio de datos (EDA) aplicando Pandas y Numpy sobre datos de clientes y de una campaña de marketing bancario, incluyendo limpieza, transformación y exploración de variables.

### 5️⃣ Power BI: Proyectos de Business Intelligence
Dos proyectos de visualización y análisis de datos en Power BI:
- **Proyecto 1:** Panel sobre PIB y deuda.
- **Proyecto 2:** Panel de ventas a partir de datos de clientes, productos, pedidos y vendedores.

### 6️⃣ Proyecto final: Felicidad mundial 2015-2019
Proyecto de principio a fin sobre los datos del *World Happiness Report* (2015-2019), con el objetivo de mostrar los datos y sus relaciones con la mayor claridad posible:
- **ETL en Python (Pandas):** unificación de cinco ficheros anuales con columnas distintas en una única tabla de 782 filas y 10 columnas.
- **Informe en Power BI de 8 hojas:** segmentador de año, análisis variable a variable, dispersiones y correlaciones con la puntuación, mapa y ranking, comparador de países, cambios entre 2015 y 2019 y conclusiones. Medidas DAX propias y paleta de colores terrosos.
- **Resultados:** la puntuación media mundial es estable (5,38 → 5,41), el PIB, el apoyo social y la esperanza de vida son los factores más ligados a la puntuación, y la generosidad casi no discrimina.

Detalle completo, pasos y limitaciones en [`6. Proyecto final/README.md`](6.%20Proyecto%20final/README.md).

## 🔄 Próximos Pasos

- Añadir los proyectos de los próximos módulos del máster a medida que se completen.
- Documentar los resultados y conclusiones de los proyectos de los módulos anteriores en su propia carpeta (el proyecto final ya lo incluye).
- Incluir gráficos/capturas del dashboard y de los resultados más relevantes.

## 🤝 Contribuciones

Este es un repositorio personal de uso académico. No obstante, cualquier sugerencia o comentario es bienvenido a través de un issue.

## ✒️ Autor

- Lucas Ochova
- [@lucasochova](https://github.com/lucasochova)
