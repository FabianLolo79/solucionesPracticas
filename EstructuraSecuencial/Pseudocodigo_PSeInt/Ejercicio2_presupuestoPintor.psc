//EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
//			  que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
//			cliente le indica que necesita conocer el costo de mano de obra para pintar una
//			pared rectangular de un galpón. El pintor cobra un monto ?jo por cada metro
//			cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
//			pintar la pared.

// ANALISIS
//	DATOS DE ENTRADA --> E
	// precio_metro_cuadrado float
	// ancho_pared float
	// alto_pared float

// PROCESO --> P
	// area_metros_cuadrados = ancho_pared * alto_pared --> calcular m2 de la pared a pintar
	// resultado_presupuesto = area_metros_cuadrados * precio_metro_cuadrado --> calcular el precio de m2 por el area_metrosCuadrados a cubrir

// SALIDA --> S
// resultado_presupuesto --> mostrar el resultado del presupuesto 

Algoritmo PresupuestoPintor
	//VARIABLES --> E
	definir precio_metro_cuadrado, alto_pared, ancho_pared Como Real
	
	Escribir "--------------------------------"
	Escribir "|    PRESUPUESTO DE PINTURA    |" 
	Escribir "|     Precio m2 : $ 3.000      |"    
	Escribir "--------------------------------"
	Escribir ""
	
	Escribir  "Ingrese los metros de alto de la pared a calcular: "
	Leer alto_pared 
	
	Escribir ""
	
	Escribir "Ingrese los metros de ancho de la pared a calcular: "
	Leer ancho_pared
	
	Escribir ""
	
	precio_metro_cuadrado = 3000 
	area_metros_cuadrados = ancho_pared * alto_pared
	
	resultado_presupuesto = area_metros_cuadrados * precio_metro_cuadrado
	
	Escribir "El presupuesto de un área de " area_metros_cuadrados " m2 a pintar es de: $ " resultado_presupuesto ".- pesos."
	
	
FinAlgoritmo
