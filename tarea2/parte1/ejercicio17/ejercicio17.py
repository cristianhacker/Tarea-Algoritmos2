""" Desarrolle un algoritmo de un enfrentamiento de 2 jugadores para un juego de RPG por roles, donde 
debemos saber cuanta vida y ataque debe tener cada uno. Debemos tener en cuenta que solo hay 2 turnos, en un turno 
solo 1 jugador puede atacar al otro, reduciendo su vida y luego debemos de cambiar de turno para que sea el turno de ataque
 del otro jugador.  El enfrentamiento debe continuar mientras que ambos jugadores tienen vida mayor a 0. Debes mostrar en un
   mensaje quién fue el ganador
"""
vida1 = 100
vida2 = 100
ataque1 =  14
ataque2 = 13

while True:
    turno = input("Ingrese 'A' para el jugador 1 y 'B' para que comienze el jugador 2: ").upper()
    if turno not in ["A", "B"]:
        print("Esa opción es invalida")
    else:
        break
    
    
while True:
    if vida1<0:
        print("El ganador es JUGADOR '2'")
        break
    elif vida2<0:
        print("El ganador es JUGADOR '1'")
        break
    else: 
        if turno == "A":
            vida2 -= ataque1
            turno = "B"
            print("\nTurno del jugador '1'")
            print(f"El ataque del jugador 1 es: {ataque1} de daño.")
            print(f"Vida restante del jugador '2' es: {vida2}")
        elif turno == "B":
            vida1 -= ataque2
            turno = "A"
            print("\nTurno del jugador '2'")
            print(f"El ataque del jugador 2 es: {ataque2} de daño.")
            print(f"Vida restante del jugador '1' es: {vida1}")
       
