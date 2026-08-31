Proceso ejercicio21
	Definir plato, lista_nombre, nombre Como Caracter
	Definir cant, gasto, precio,i Como Entero
	Escribir "Ingrese el nombre del plato: "
	Leer plato
	Escribir "¿Cuántos productos se necesitan comprar?: "
	Leer cant
	Dimension lista_nombre[cant]
	gasto = 0
	Para i = 1 Hasta cant con Paso 1 Hacer
		Escribir "Ingrese el nombre de ", i, " producto: "
		Leer nombre
		escribir "Ingrese el precio del producto ",nombre
		Leer precio
		gasto = gasto + precio
		Escribir "El gasto acumulado hasta ahora es: ", gasto, " $."
	FinPara
	
	
	
FinProceso
