print("-------------------------------")
print("|        CALCULAR IVA         |")
print("|            v2.0             |")
print("-------------------------------")

precio = float(input("Ingrese el precio a consultar: "))

print("")

iva = float(input("Ingrese el monto del iva correspondiente (10.5 ó 21): "))

print("")

precio_con_iva = precio * iva / 100 + precio 

print("++++++++++++++++++++++++++++++++++++++")
print("")
print(f"El precio con IVA es ${precio_con_iva}")
print("")
print("++++++++++++++++++++++++++++++++++++++")
print("")
print("")
print("")