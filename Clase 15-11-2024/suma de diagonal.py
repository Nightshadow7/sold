# Define una matriz 3x3 como lista de listas. Escribe un programa para sumar los elementos de la diagonal
# principal de la matriz
def impresion(matriz, argumento):
  print(f"La {argumento} es: ")
  for i in range(len(matriz)):
    print(matriz[i])
# Defino la matriz
matriz = [[1, 2, 3] , [4, 5, 6] , [7, 8, 9]]

# sumar los elementos de la diagonal principal
suma_diagonal = 0
for i in range(len(matriz)):
  suma_diagonal += matriz[i][i]

impresion(matriz, "matriz")
print(f"La suma de la diagonal es: {suma_diagonal}")