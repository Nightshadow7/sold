import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Crear un dataframe de ejemplo con 50 registros
data = {
  'ID': [f"ID{str(i).zfill(3)}" for i in range(1, 51)],
  'producto': [f"prodcto {i}" for i in range(1, 51)],
  'cantidad': [i*2 for i in range(1, 51)]
}

df = pd.DataFrame(data)

# Mostrar las primeras filas del dataframe
print("")
print(df.head)

# Configuracion para la visualizacion
plt.figure(figsize=(10 ,6 )) #Tamaño de la figura

# Crear la grafica de barras usando seaborn
sns.barplot(x='producto' , y='cantidad' , data=df , palette="magma")

# Rotar las etiquetas del eje X para que sean legibles
plt.xticks(rotation=90)

# Titulos y etiquetas de los ejes
plt.title("Cantidad de Producto")
plt.ylabel("Cantidad")
plt.xlabel("Producto")

# Mostrar grafica
plt.tight_layout() #Ajustar el layout para evitar que las etiquetas se corten
plt.show()