"""Desarrolle un algoritmo que simule al juego adivine un número y tengas 3 opciones para adivinar, para ello debes definir un número 
fijo que se debe de adivinar o que sea aleatorio del 1 al 20. Debes pedir ingresar un número a adivinar. Si ingresas un número menor debes
 mostrar el mensaje “El número a adivinar es mayor, vuelve a intentarlo”. Si ingresas un número mayor debes mostrar el mensaje “El número 4
 a adivinar es menor, vuelve a intentarlo”. Si adivinas muestra el mensaje “Adivinaste 
el número. Utilizaste ”, numero, “ de intentos”"""
import random
adivinar = random.randint(1,20)
max_intentos = 4
intentos = 0
while max_intentos>0:
    user = int(input("Ingrese un número: "))
    max_intentos -= 1
    intentos +=1
    if user == adivinar:
        print(f"¡Ganaste! Lo hiciste en {intentos} intentos")
    elif max_intentos == 0:
        print("Perdiste :(")
    else:
        if user > adivinar:
            print("El número es menor")
        else:
            print("El numero es mayor")