Proceso ejercicio2
	Definir oper Como Cadena
	Definir cant, resultado, i, lista Como Entero
	Definir break Como Lógico
	Escribir ' S = Suma'
	Escribir ' R = Resta'
	Escribir ' M = Multiplicación'
	break <- Verdadero
	Mientras break Hacer
		Escribir 'Seleccione una opción: '
		Leer oper
		oper <- Mayusculas(oper)
		Si oper=='S' O oper=='R' O oper=='M' Entonces
			break <- Falso
		SiNo
			Escribir 'Ingrese una opción válida'
		FinSi
	FinMientras
	Escribir 'Ingrese una cantidad de números: '
	Leer cant
	Dimensionar lista(cant)
	Para i<-0 Hasta cant-1 Con Paso 1 Hacer
		Escribir 'Ingrese el ', i+1, ' número'
		Leer lista[i]
	FinPara
	Si oper=='S' Entonces
		resultado <- 0
		Para i<-0 Hasta cant-1 Con Paso 1 Hacer
			resultado <- resultado+lista[i]
		FinPara
	SiNo
		Si oper=='R' Entonces
			resultado <- lista[0]
			Para i<-1 Hasta cant-1 Con Paso 1 Hacer
				resultado <- resultado-lista[i]
			FinPara
		SiNo
			resultado <- 1
			Para i<-0 Hasta cant-1 Con Paso 1 Hacer
				resultado <- resultado*lista[i]
			FinPara
		FinSi
	FinSi
	Escribir 'El resultado de ', oper, ' es: ', resultado
FinProceso
