"""Desarrolle un algoritmo donde ingrese la cantidad de productos y sus respectivos precios en un arreglo, 
para la preparación de un plato, también se debe mostrar al final el costo a gastar.
-Ingresar el plato: arroz con pollo
-¿Cuántos productos se necesitan comprar?:cantidad  2         
Dimension nombre[cantidad]
Dimension precio[cantidad]
gasto

Según la cantidad ingresada, si es 2, debe preguntar
-Ingrese nombre de producto:  nombre[0]		pollo
-Ingrese precio de producto:  precio[0]		8
-gasto=gasto + precio[0]

-Ingrese nombre de producto: nombre[1]		arroz
-Ingrese precio de producto: precio[1]		2
gasto= gasto precio[1]
"""
plato=input("Ingrese el nombre del plato: ")
cant = int(input("¿Cuántos productos se necesitan comprar?: "))
lista_nombre = []
lista_precio =[]
gasto = 0
for i in range(cant):
    nombre = input(f"{i+1}.\nIngrese el nombre del {i+1} producto: ")
    lista_nombre.append(nombre)
    precio = int(input(f"Ingrese el precio del producto {nombre} : "))
    lista_precio.append(precio)
    gasto += precio
    print(f"\033[1mEl gasto acumulado hasta ahora es: {gasto} $\033[0m")

for j in range(cant):

    print(lista_nombre[j], "=" , lista_precio[j])
print(f"\033[1mLa lista de ingredientes es: {lista_nombre}\nEl precio total es: {gasto} $\033[0m")




