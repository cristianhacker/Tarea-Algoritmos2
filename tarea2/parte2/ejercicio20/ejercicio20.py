"""Realice un pseudocódigo, que realice lo siguiente
Debe preguntar ¿Cuántos elementos desea que tenga su array?
La respuesta debe almacenarla en la cantidad de elementos de un array
Debe ingresar dato para cada elemento del array 
Debe imprimir todos los datos de los elementos del array
"""
lista = []
cant = int(input("Ingrese una cantidad de elementos para el array: "))
for i in range(cant):
    lista.append(input(f"Ingrese un elemento para la posición {i} del array: "))
    print(lista)
    