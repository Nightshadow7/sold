# Taller de Análisis de Datos

## Introducción
En el presente taller, se analizarán algunas de las librerías de Python más utilizadas en el campo del análisis de datos. Para cada librería se presentarán su definición, sus campos de aplicación y algunos de sus métodos más usados.

## Librerías de Python para Análisis de Datos

### NumPy

__¿Qué es?__

NumPy es una librería de Python diseñada para realizar operaciones matemáticas y de álgebra lineal de manera eficiente. Es especialmente útil para trabajar con grandes arreglos y matrices multidimensionales, y proporciona una variedad de funciones matemáticas para la manipulación de datos numéricos.

__Campos de aplicación:__

NumPy se utiliza principalmente en:

1. Análisis de datos numéricos y estadísticos
2. Procesamiento de señales
3. Computación científica
4. Simulaciones numéricas y de sistemas físicos

**Métodos más utilizados:**

  + np.array() — **Crea arreglos.**
  + np.zeros() y np.ones() — **Crea arreglos de ceros o unos.**
  + np.arange() — **Crea arreglos con un rango de valores.**
  + np.reshape() — **Cambia la forma de un arreglo.**
  + np.dot() — **Realiza el producto escalar de dos arreglos.**


### Pandas

__¿Qué es?__

Pandas es una librería de Python que facilita el manejo y análisis de datos estructurados. Proporciona estructuras de datos como **DataFrame** y **Series**, permitiendo la manipulación de datos tabulares de forma sencilla.

__Campos de aplicación:__

Pandas es ampliamente utilizada en:

	1. Limpieza y preprocesamiento de datos
	2. Análisis de series temporales
	3. Manejo y manipulación de grandes conjuntos de datos
	4. Generación de reportes de datos y agregación de estadísticas

**Métodos más utilizados:**

  + pd.DataFrame() — **Crea un DataFrame.**
  + pd.read\_csv() — **Carga datos desde un archivo CSV.**
  + df.head() y df.tail() — **Muestra las primeras o últimas filas de un DataFrame.**
  + df.describe() — **Genera estadísticas descriptivas de un DataFrame.**
  + df.groupby() — **Agrupa datos en un DataFrame.**

### Matplotlib.pyplot

__¿Qué es?__

Matplotlib es una librería de visualización de datos en Python. Su módulo **pyplot** proporciona una interfaz similar a la de MATLAB para la creación de gráficos de datos, como histogramas, gráficos de líneas, gráficos de dispersión, entre otros.

__Campos de aplicación:__

Matplotlib.pyplot es utilizada en:

  1. Visualización de datos en investigaciones científicas
  2. Generación de gráficos para análisis exploratorio de datos
  3. Creación de visualizaciones personalizadas en aplicaciones de análisis de datos

__Métodos más utilizados:__

  + plt.plot() — **Crea gráficos de líneas.**
  + plt.scatter() — **Crea gráficos de dispersión.**
  + plt.hist() — **Genera histogramas.**
  + plt.xlabel() y plt.ylabel() — **Etiqueta los ejes.**
  + plt.title() — **Añade un título al gráfico.**


### Scikit-Learn (sklearn)

__¿Qué es?__

Scikit-Learn, también conocida como **sklearn**, es una librería de Python para aprendizaje automático. Ofrece herramientas y algoritmos para clasificación, regresión, reducción de dimensionalidad y agrupamiento de datos.

__Campos de aplicación:__
    
Scikit-Learn es utilizada en:

  1. Desarrollo de modelos de aprendizaje supervisado y no supervisado
  2. Procesamiento y selección de características
  3. Validación y evaluación de modelos
  4. Optimización de hiperparámetros en modelos de machine learning

__Métodos más utilizados:__

  + train\_test\_split() — **Divide los datos en conjuntos de entrenamiento y prueba.**
  + StandardScaler() — **Estandariza las características.**
  + fit() y predict() — **Ajusta y predice usando modelos de aprendizaje automático.**
  + cross\_val\_score() — **Realiza validación cruzada en modelos.**
  + GridSearchCV() — **Optimiza hiperparámetros usando búsqueda en cuadrícula.**
