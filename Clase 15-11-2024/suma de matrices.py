# 4. Define dos matrices 2x2 como listas de listas. Realiza la suma de estas matrices sin usar librerias adicionales

# Definir dos matrices
matriz1 = [[1 , 2 , 3] , [3 , 4 , 5] , [5 , 6 , 7]]
matriz2 = [[7 , 8 , 9] , [10 , 11 , 12] , [13 , 14 , 15]]
matriz3 = [[7 , 8 , 9] , [10 , 11 , 12] , [13 , 14 , 15]]

# Suma de matrices
suma_de_matrices = [[matriz1[i][j] + matriz2[i][j] + matriz3[i][j] 
  for i in range(len(matriz1))]
  for j in range(len(matriz1))]

print (f"La suma de las 2 matrices es: {suma_de_matrices}")