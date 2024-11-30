# Crea dos listas que representen vectores y realiza la resta elemento por elemento manualmente
# Definir el vector
vector1 = [10, 20 , 30 , 40 , 50 , 60 , 70 , 80]
vector2 = [5, 10, 15, 20, 25, 30, 35, 40]

# resta de vector elemento por elemento
resta = [ vector1[i]-vector2[i] for i in range(len(vector1))]

print(f"La resta de los vectores {vector1} - {vector2} = {resta}")