import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
# Crear un DataFrame de ejemplo

data = {
  'Nombre': ['Ana', 'Luis', 'Juan', 'María', 'Pedro'],
  'Edad': [23, pd.NA, 35, pd.NA, 28],
  'Ciudad': ['Madrid', 'Barcelona', pd.NA, 'Valencia', 'Sevilla']
}  
df = pd.DataFrame(data)

# Visualizar datos faltantes
msno.matrix(df)
plt.show()

# También puedes usar el gráfico de barras
msno.bar(df)
plt.show()