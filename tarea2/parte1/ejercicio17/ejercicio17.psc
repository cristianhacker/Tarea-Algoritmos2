Proceso ejercicio17
	Definir vida1, vida2, ataque1, ataque2 Como Entero
	Definir turno Como Caracter
	Definir opc_validada, opc_vida Como Logico
	opc_validada = Verdadero
	vida1 = 100
	vida2 = 100
	ataque1 = 14
	ataque2 = 13
	Mientras opc_validada = Verdadero Hacer
		Escribir "Ingrese A para el jugador 1 y B para que comienze el jugador 2: "
		Leer turno
		turno = Mayusculas(turno)
		Si turno <> "A" Y turno <> "B" Entonces
			Escribir "Esa opcion es invalida"
		Sino 
			opc_validada = Falso
		FinSi
	FinMientras
	opc_vida = Verdadero
	Mientras opc_vida == Verdadero Hacer
		Si vida1 <0 Entonces
			Escribir "El ganador es el JUGADOR 2"
			opc_vida = Falso
		Sino 
			Si vida2 <0 Entonces
				Escribir "El ganador es el JUGADOR 1"
				opc_vida = Falso
			SiNo 
				Si turno == "A" Entonces
					vida2 = vida2 - ataque1
					turno = "B"
					Escribir "Turno del jugador -1-"
					Escribir "Ataque de JUGADOR 1: " ataque1 " de daño"
					Escribir "La vida restante del jugador -2- es: ", vida2
				SiNo 
					vida1 = vida1- ataque2
					turno = "A"
					Escribir "Turno del jugador -2-"
					Escribir "Ataque de JUGADOR 2: " ataque2 " de daño"
					Escribir"La vida restante del jugador -1- es: " vida1
					
				FinSi
			FinSi
		FinSi
	FinMientras
	
	
	
FinProceso
