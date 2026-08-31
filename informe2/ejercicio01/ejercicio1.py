"""Desarrolle un algoritmo en Pseudocódigo y programa en Python donde ingrese cantidad de elementos que debe 
tener el arreglo y luego ingresar debe números enteros por cada elemento. Debe imprimir el número mayor de todos los elementos}
 del arreglo o lista."""
cant = int(input("Ingrese la cantidad de números: "))
lista = []

for i in range(cant):
    lista.append(int(input("Ingrese un número: ")))

print(f"La lista de números es: {lista}")
print(f"El mayor de la lista es: {max(lista)}")
      

cantidad = int(input("ingrese una cantidad de numeros: "))
listas = []
for j in range(cant):
    listas.append(int(input(f"Ingrese el {i +1} número:  ")))
mayor = listas[0]
for h in listas:
    if h > mayor:
        mayor = h
print(f"La lista de números es: {listas}")
print(f"El mayor de la lista es: {mayor}")
      




