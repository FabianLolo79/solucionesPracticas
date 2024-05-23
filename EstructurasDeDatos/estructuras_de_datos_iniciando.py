"""
Actividades parte 1: Iniciando
Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos 
(variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

    1. Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas,
        guardarlos en una lista y mostrarlos. 

    2. Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo.

    3. Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

    4. En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos 
        (nombre, apellido, dni, email, fecha de nacimiento).

    5. Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). 
        Luego mostrar los datos de la tupla.

Nota: para saber si el número i es par hacer i % 2 == 0

"""

# Ejercicio 1
print("")
print("Ejercicio 1")
print("")
lista_nombres = []

nombre = input("Ingrese un nombre: ")

while len(lista_nombres) < 10:
        
        if nombre not in lista_nombres:
            lista_nombres.append(nombre)
        nombre = input("Ingrese un nombre: ")

print("")
print("")
print(lista_nombres)
print("")
print("")


# Ejercicio 2
print("Ejercicio 2")

lista_nombres.pop(2)
print(f"Borrado del elemento 3 {lista_nombres}")
print("")
print("")

lista_nombres.pop(-1)
print(f"Borrado del último elemento {lista_nombres}")
print("")
print("")

lista_nombres.sort()
print(f"Ordenado alfabeticamente {lista_nombres}")
print("")
print("")

print("")
print("")


# Ejercicio 3


