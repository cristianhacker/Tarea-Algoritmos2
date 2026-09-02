Proceso ejercicio20
	Definir cant, i Como Entero
	Definir elemento, lista Como Cadena
	Escribir '¿Cuántos elementos desea que tenga su array?'
	Leer cant
	Dimensionar lista(cant)
	Para i<-0 Hasta cant-1 Con Paso 1 Hacer
		Escribir 'Ingrese un elemento para la posición ', i, ' del array: '
		Leer lista[i]
	FinPara
	Para i<-0 Hasta cant-1 Con Paso 1 Hacer
		Escribir lista[i]
	FinPara
FinProceso
