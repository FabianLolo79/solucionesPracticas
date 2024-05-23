Algoritmo CalcularIVA_mejorado
	
	Escribir "Ingrese el precio de lista a consultar: " 
	
	Leer precio
	
	Escribir "Ingrese el IVA correspondiente (10.5 ó 21): "
	
	Leer iva
	
	precio_con_iva <- precio * iva / 100 + precio 
	
	Escribir "El precio con IVA es: " precio_con_iva
	
FinAlgoritmo
