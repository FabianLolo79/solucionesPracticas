""" 
EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared.

"""

"""
    ANALISIS
	DATOS DE ENTRADA --> E
        precio_metro_cuadrado float
        ancho_pared float
        alto_pared float

    PROCESO --> P
        area_metros_cuadrados = ancho_pared * alto_pared # calcular m2 de la pared a pintar
        resultado_presupuesto = area_metros_cuadrados * precio_metro_cuadrado # calcular el precio de m2 por el area_metros_cuadrados a cubrir

    SALIDA --> S
        resultado_presupuesto// mostrar el resultado del presupuesto
"""

print("-------------------------------")
print("|    PRESUPUESTO DE PINTURA   |")
print("|                             |")
print("-------------------------------")

print("")
# Variables ENTRADA
precio_metro_cuadrado = float(input("Ingrese el precio por m2: "))
alto_pared = float(input("Ingrese los metros de alto de la pared a calcular: "))
ancho_pared = float(input("Ingrese los metros de ancho de la pared a calcular: "))
print("")
print("----------------------------------------------------------------------------------")
print("")

# PROCESOS
area_metros_cuadrados = ancho_pared * alto_pared
resultado_presupuesto = area_metros_cuadrados * precio_metro_cuadrado

# SALIDA
print(f"El presupuesto de un área de {area_metros_cuadrados} m2 a pintar es de: $ {resultado_presupuesto} pesos.")
print("")
print("----------------------------------------------------------------------------------")
print("")
print("")



