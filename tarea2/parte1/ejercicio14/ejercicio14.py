"""Elabora un algoritmo que permita ingresar letras del alfabeto. El algoritmo terminará cuando se ingrese la letra x.
 Utiliza la estructura MIENTRAS"""
letra = str(input("INGRESE UNA LETRA DEL ALFABETO: "))
while letra != "x":
    print("LETRA INCORRECTA.")
    letra = str(input("INGRESE UNA LETRA DEL ALFABETO: "))
print("Saliste del bucle")