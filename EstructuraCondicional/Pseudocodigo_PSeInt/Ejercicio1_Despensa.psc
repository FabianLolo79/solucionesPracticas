// Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
//  Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%.
// Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados.
// La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos).
// Desarrolle una solución algorítmica para saber cuento debe pagar el cliente. 
//

// ENTRADA 
	// precio_leche = 1000 float x 1 unidad 
	// cantidad_producto  de 1 a 11 unidades  
	// cantidad_producto  de 12 a 24 unidades desc 10%
	// si + 24 unidades des 15%
	// jubilado boolean desc 10%
	//  precio_final
	// precio_con_descuento 

// PROCESOS
  // cantidad_producto 
 //	


// SALIDA
	// precio_descuento 








Algoritmo calculo_descuento
	definir precio_leche, cantidad_producto, descuento, precio_con_descuento, precio_final Como Real
	definir  jubilado Como Logico
	Definir  respuesta Como Caracter
	
	precio_leche = 1000	
	cantidad_producto = 0 
	descuento = 0
		
	Escribir "Ingrese la cantidad de unidades de leche comprada: "
	Leer cantidad_producto
	Escribir ""
	
	Escribir "¿Es usted jubilada/o? (s/n): "
	Leer respuesta
	
	Si respuesta = "s" Entonces
		jubilado = Verdadero
		
	FinSi
	Si respuesta = "n" Entonces
		jubilado = falso
	FinSi
	
	Si cantidad_producto > 0 O cantidad_producto <= 11 Entonces
		precio_final = cantidad_producto * precio_leche
	FinSi
		
	Si cantidad >= 12  y cantidad <= 24 Entonces
		descuento = 10
		Si jubilado Entonces 
			descuento = descuento + 10 
			precio_con_descuento = precio_leche - (precio_leche * descuento / 100)	
			precio_final = precio_leche - precio_con_descuento
			Escribir "El precio a pagar es:" precio_final
		SiNo			
			precio_con_descuento = precio_leche - (precio_leche * descuento / 100)
			precio_final = precio_leche - precio_con_descuento
			Escribir "El precio a pagar es:" precio_final
		FinSi
//		Escribir "El precio a pagar es:" precio_final
	Fin si
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
//	Si cantidad > 24 Entonces
//		descuento = 15 
//		Si jubilado Entonces 
//			descuento = descuento + 10 
//			precio_con_descuento = precio_leche - (precio_leche * descuento / 100)
//		FinSi
//		precio_con_descuento =  precio_leche - (precio_leche * descuento / 100) 
//	Fin Si
	
//	Escribir "El precio a pagar es:" precio_final
	
	
FinAlgoritmo
