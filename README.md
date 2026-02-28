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
└── README.md
