"""
Crear una lista de 5 números al azar de 0 a 9, que estén ordenados y no repetidos.
"""

import random

#Declaro la lista
numeros = []

# generar número al azar del 0 al 9 
numero_generado = random.randint(0,9)

#Cargar números 
while len(numeros) <= 4:
    if numero_generado not in numeros: # Conprueba que no esté repetido antes de cargar
        numeros.append(numero_generado)
    numero_generado = random.randint(0,9)   

#Ordenar la lista
numeros.sort()

print(numeros)


