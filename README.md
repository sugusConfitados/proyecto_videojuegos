# 🎮 Video Games Sales Analysis & Prediction

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📌 Visión General
Este repositorio contiene un análisis exhaustivo del mercado global de videojuegos basado en datos históricos de ventas. El objetivo principal es transformar datos brutos en **inteligencia de negocios**, identificando qué factores (plataforma, género, región) determinan el éxito comercial de un título.

El proyecto culminará con el desarrollo de un modelo de **Machine Learning** para predecir las ventas globales.

## 🎯 Objetivos Estratégicos
- [ ] **Limpieza de Datos:** Tratar valores nulos en `Year` y `Publisher`.
- [ ] **Análisis Regional:** Comparar el comportamiento de los mercados de NA, EU y JP.
- [ ] **Identificación de Tendencias:** Analizar la evolución de géneros y plataformas por décadas.
- [ ] **Modelado Predictivo:** Implementar algoritmos de regresión para estimar `Global_Sales`.

## 📂 Estructura del Proyecto
```text
proyecto_videojuegos_ventas/
├── data/               # Dataset original (vgsales.csv) y procesados.
├── notebooks/          # Jupyter Notebooks organizados por etapas.
│   ├── 01_eda_and_cleaning.ipynb
│   ├── 02_regional_analysis.ipynb
│   └── 03_model_training.ipynb
├── src/                # Funciones auxiliares en scripts de Python.
├── models/             # Modelos de ML entrenados (.pkl).
├── reports/            # Gráficos y visualizaciones exportadas.
└── README.md.

## Rodamap

🗺️ Hoja de Ruta: Video Games Market Insights & Predictive AnalyticsFase 
- [ ] **Fase 1**: Cimentación y Calidad de Datos (Completada ✅)
  Objetivo: Asegurar que los datos sean confiables.
  Hitos:Estructura de carpetas profesional y control de versiones (Git/GitHub).
  Diagnóstico inicial: Análisis de nulos, duplicados y tipos de datos.
  Limpieza (Data Wrangling): Normalización de encabezados, eliminación de nulos en year, imputación de publisher y casting de tipos.

- [ ] Fase 2: Inteligencia de Mercados Regionales (En curso 🕒)
  Objetivo: Entender el comportamiento del consumidor en $NA$ (Norteamérica), $EU$ (Europa) y $JP$ (Japón).
  Acciones:
  Market Share: Cálculo del peso relativo de cada región sobre las ventas globales.
  Preferencia de Género: Identificar por qué ciertos géneros (ej. RPG en Japón) dominan mercados específicos.
  Dominio de Plataformas: Análisis de la penetración de hardware por región.
  KPI: Ventas Totales por Región ($Sales_{Total} = \sum Sales_{Region}$).

- [ ] Fase 3: Dinámicas Temporales y Ciclos de VidaObjetivo: 
  Analizar cómo ha evolucionado la industria desde 1980 hasta la actualidad.
  Acciones:
  Análisis de Series Temporales: ¿En qué año alcanzó la industria su pico de ventas?
  Ciclo de Vida de Consolas: Visualizar el auge y caída de plataformas (ej. PS2 vs Wii vs PS4).
  Evolución de Géneros: Ver cómo el mercado se movió de las plataformas (80s) a la acción y shooters (actualidad).

- [ ] Fase 4: Ingeniería de Variables (Feature Engineering)
  Objetivo: Traducir los datos crudos a un formato que el algoritmo de Machine Learning pueda "entender".
  Acciones:
  Encoding: Convertir variables categóricas (genre, platform) en valores numéricos.
  Escalamiento: Normalizar los datos si es necesario.
  Tratamiento de Outliers: Decidir qué hacer con los "Super-ventas" (Wii Sports, GTA V) para no sesgar el modelo.
  Creación de variables: Quizás crear una variable "Años en el mercado".

- [ ] Fase 5: Modelado Predictivo (Machine Learning)
  Objetivo: Desarrollar un algoritmo que prediga las ventas globales de un nuevo lanzamiento.
  Acciones:
  Selección de Modelos: Probar Regresión Lineal, Random Forest y posiblemente XGBoost.
  Split de Datos: Dividir en set de entrenamiento ($Train$) y prueba ($Test$).
  Métricas de Éxito: Evaluar el error mediante $RMSE$ (Root Mean Squared Error) y $R^2$.

- [ ] Fase 6: Optimización e Insights de Negocio
  Objetivo: Ajustar el modelo y extraer conclusiones accionables para los directivos.
  Acciones:
  Feature Importance: ¿Qué influye más en el éxito de un juego? ¿El género o la plataforma?
  Ajuste de Hiperparámetros: Optimizar el modelo para reducir el error.
  Conclusiones Finales: "Si vas a lanzar un juego de Acción en Japón, hazlo en esta plataforma específica".

- [ ] Fase 7: Entrega Final y Visualización Ejecutiva
  Objetivo: Presentar los hallazgos de forma que un CEO pueda tomar decisiones.
  Acciones:
  Creación de un Dashboard final (o visualizaciones de alto impacto en Seaborn/Plotly).
  Actualización final del README.md con los resultados del modelo.
  Presentación de "Hallazgos Accionables".