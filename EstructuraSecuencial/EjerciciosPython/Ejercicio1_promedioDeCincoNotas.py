""" 
EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada

materia y quiere saber cuál es su promedio.
"""

"""
    ANALISIS
	DATOS DE ENTRADA --> E
        nota_1, nota_2, nota_3, nota_4, nota_5 float 
    
    PROCESO --> P
        suma = nota_1 + nota_2 + nota_3 + nota_4 + nota_5 
        promedio = suma / 5

    SALIDA --> S
        promedio --> mostrar el resultado del promedio
"""


print("-------------------------------")
print("|           CÁLCULO           |")
print("|           PROMEDIO          |")
print("-------------------------------")

print("")

nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))
nota_4 = float(input("Ingrese la cuarta nota: "))
nota_5 = float(input("Ingrese la quinta nota: "))

suma = nota_1 + nota_2 + nota_3 + nota_4 + nota_5

promedio = suma / 5

print("")
print(f"El promedio de las cinco notas es: {promedio}")
print("")
print("")
print("_____________________________________")