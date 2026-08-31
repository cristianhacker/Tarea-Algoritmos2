Proceso ejercicio1
	Definir cant, i, num_mayor, lista Como Entero
	Escribir 'Ingrese una cantidad de números: '
	Leer cant
	Dimensionar lista(cant)
	Para i<-0 Hasta cant-1 Con Paso 1 Hacer
		Escribir 'Digite el ', i+1, ' número: '
		Leer lista[i]
	FinPara
	num_mayor <- lista[0]
	Para i<-0 Hasta cant-1 Con Paso 1 Hacer
		Si lista[i]>num_mayor Entonces
			num_mayor <- lista[i]
		FinSi
	FinPara
	Escribir 'El número mayor es: ', num_mayor
FinProceso
