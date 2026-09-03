from functools import reduce

operacion = input("Ingrese la operación a realizar (S, R, M): ")
while operacion != "S" and operacion != "R" and operacion != "M":
    print("Operación invalida. Ingrese una de las siguientes: S, R, M")
    operacion = input("Ingrese la operación a realizar (S, R, M): ")
cant = int(input("Ingrese la cantidad de números a operar: "))
list = []
if operacion == "S":
    for i in range(0,cant):
        num = int(input("Ingrese un número: "))
        list.append(num)
    print("El número suma de la lista es: ", sum(list))
elif operacion == "R":
    for i in range(0,cant):
        num = int(input("Ingrese un número: "))
        list.append(num)
    print("El número resta de la lista es: ", reduce(lambda x, y: x - y, list))
elif operacion == "M":
    for i in range(0,cant):
        num = float(input("Ingrese un número: "))
        list.append(num)
    print("El número multiplicado de la lista es: ", reduce(lambda x, y: x * y, list))

