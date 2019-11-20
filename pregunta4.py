import math
import random
while True:
    fila = int(input("Ingrese la cantidad de filas: "))
    columna = int(input("Ingrese la cantidad de columnas: "))

    if columna < 1 and columna > 5 and fila < 1 and fila > 5:
        print("Debe ser numeros entre 2 y 5")
    else:
        matriz = []

        for i in range (columna**fila):
            a = random.randint(1,100)
            if (a%2 == 0):
                contar = matriz.count(i)
            matriz.append([a])
            
            


        print(matriz)
        print("Hay ", contar, "numeros pares")