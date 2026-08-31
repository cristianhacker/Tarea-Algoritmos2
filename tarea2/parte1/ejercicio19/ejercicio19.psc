Proceso ejercicio19
	Definir adivinar, intentos,max_intentos, user Como Entero
	adivinar = 6
	max_intentos = 4
	intentos = 0
	Mientras max_intentos > 0 Hacer
		Escribir "Ingrese un número del 1 al 20: "
		Leer user
		max_intentos = max_intentos -1
		intentos = intentos + 1
		Si user == adivinar Entonces
			Escribir "¡Ganaste! Lo hiciste en ", intentos, " intentos."
		SiNo
			Si max_intentos = 0
				Escribir "Perdiste :("
			SiNo
				Si user > adivinar Entonces
					Escribir "El número es menor"
				SiNo
					Escribir "El número es mayor"
				FinSi
			FinSi
		FinSi
	FinMientras
	
FinProceso
