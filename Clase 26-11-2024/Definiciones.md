# MinMaxScaler
### Definición:
__MinMaxScaler()__ es una técnica de preprocesamiento utilizada para normalizar los valores de una columna de datos dentro de un rango específico (por defecto, entre 0 y 1).
La fórmula utilizada es:
\[
X_{\text{scaled}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}
\]
Donde:
  + \( X_{\text{min}} \) es el valor mínimo de los datos.
  + \( X_{\text{max}} \) es el valor máximo de los datos.
  + \( X_{\text{scaled}} \) representa el valor normalizado.
#### Uso común: 
Se utiliza en modelos de Machine Learning sensibles a las escalas, como redes neuronales y algoritmos de clustering.

# StandardScaler()
### Definición: 
__StandardScaler()__ es una técnica de preprocesamiento que transforma los datos para que tengan una media de 0 y una desviación estándar de 1.
La fórmula utilizada es:
\[
X_{\text{scaled}} = \frac{X - \mu}{\sigma}
\]
Donde:
  + \( \mu \) es la media de los datos.
  + \( \sigma \) es la desviación estándar de los datos.
  + \( X_{\text{scaled}} \) representa el valor estandarizado.

#### Uso común: 
Se emplea en algoritmos como SVM, PCA y regresiones lineales, que dependen de la escala de los datos.


# Apply()
### Definición: 
__apply()__ es una función de la librería pandas que permite aplicar una función personalizada a cada elemento, fila o columna de un DataFrame o Series. 
Parámetros principales:

  + La función que se aplicará.
  + Determina si la función se aplica por fila o por columna.

#### Uso común:
Realizar transformaciones personalizadas, cálculos entre columnas o filas, y categorizar datos.


## Diferencias clave:
| Funcion | Proposito Principal | Uso |
|----|----|----|
| __MinMaxScaler()__ | Normaliza valores a un rango específico (por defecto [0, 1]). | Preprocesamiento en ML. |
| __StandardScaler()__ | Estandariza valores a media 0 y desviación estándar 1. | Preprocesamiento en ML. |
| __Apply()__ | Aplica una función personalizada a elementos, columnas o filas en un __DataFrame__ o __Series__. | Transformaciones personalizadas. |


# Método del Rango Intercuartílico (IQR)
### Definición: 
El método del rango intercuartílico (IQR, por sus siglas en inglés) es una técnica estadística para identificar valores atípicos (outliers) en un conjunto de datos. Estos valores son aquellos que se encuentran significativamente fuera del rango de los datos centrales.

__Cálculo del IQR:__
\[
IQR = Q3 - Q1
\]
Donde:

  + \( Q1 \): Primer cuartil o percentil 25 (\( 25\% \) de los datos son menores o iguales a este valor).
  + \( Q3 \): Tercer cuartil o percentil 75 (\( 75\% \) de los datos son menores o iguales a este valor).
  + \( IQR \): Rango intercuartílico, que mide la dispersión de los datos.


__Límites para detectar outliers:__
\[
\text{Límite Inferior} = Q1 - 1.5 \cdot IQR
\]
\[
\text{Límite Superior} = Q3 + 1.5 \cdot IQR
\]

Un dato es considerado un outlier si cumple alguna de las siguientes condiciones:

  + Es menor que el límite inferior.
  + Es mayor que el límite superior.

#### Manejo de Outliers
Existen varias estrategias para manejar los valores atípicos identificados:

  + Eliminación: Remover las filas que contienen datos fuera de los límites definidos.
  + Transformación: Sustituir los valores atípicos por los límites superior o inferior.
  + Imputación: Rellenar los valores atípicos con un valor estadístico (media, mediana, etc.).


#### Visualización de Outliers
La detección de valores atípicos se puede complementar con gráficos, como:

  + Diagramas de caja boxplots: Permiten identificar visualmente los valores que se encuentran fuera del rango intercuartílico.
  + Histogramas: Muestran la distribución de los datos para observar posibles anomalías.


| Estrategia | Ventajas | Desventajas |
|---|---|---|
| Eliminación | Sencilla de implementar y asegura un conjunto de datos limpio. | Puede llevar a la pérdida de información importante, especialmente si los datos son escasos. |
| Transformación | Preserva los datos en el conjunto. | Puede introducir sesgos al alterar valores extremos. |
| Imputación | Utiliza valores estadísticos para mantener el tamaño del conjunto de datos. | Puede distorsionar la distribución real de los datos. |


