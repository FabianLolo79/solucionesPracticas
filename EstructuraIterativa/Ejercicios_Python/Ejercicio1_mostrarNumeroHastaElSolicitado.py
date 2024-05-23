"""
Ejercicio 1
Mostrar los números desde el 0 al número solicitado al usuario (input)
"""

"""
EPS
Entrada
numero_usuario -- entero

Proceso 
contador -- entero
verificar con while 

Salida
numero del 0 hasta el numero_usuario

"""
print("")

print("___________________________________________")
numero_usuario = int(input("Ingrese un número entero positivo: "))

contador = 0

while contador <= numero_usuario:
    print(contador)
    contador = contador + 1

print("")

print("___________________________________________")


