# 4. Define una matriz 2x2 como lista de listas y encuentra su traspuesta, es decir, intercambia las 
# filas con las columnas
def impresion(matriz, argumento):
  print(f"La {argumento} es: ")
  for i in range(len(matriz)):
    print(matriz[i])
# Definir la Matriz
matriz = [[1 , 2 , 3 , 4] , [3 , 4 , 5 , 6] , [6 , 7 , 8 , 9] , [9 , 10 , 11 , 12] , [13 , 14 , 15 , 16]]

# trasponer la matriz
traspuesta = [[matriz[i][j]
  for i in range(len(matriz))]
  for j in range(len(matriz[0]))]

impresion(matriz, "matriz")
impresion(traspuesta, "traspuesta")