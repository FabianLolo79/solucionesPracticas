""" 
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente
"""

"""
Entrada
    cantidad_producto

Proceso
    calculo cantidad + descuento

Salida
    precio_final

"""

print("-------------------------------")
print("|         Despensa            |")
print("-------------------------------")

precio_final = 0
precio_leche = 1000

cantidad_producto = int(input("Ingrese la cantidad de productos: "))
print("")
print("")
print("")

if cantidad_producto <= 11:
    precio_final = cantidad_producto * precio_leche
    print(f"EL precio a pagar es de : {precio_final}") 

#NO ME SALIÓ

