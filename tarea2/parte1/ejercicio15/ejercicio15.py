"""Elabora un algoritmo que permita ingresar números enteros. El algoritmo 
terminará cuando la suma de los números ingresados sea mayor a 100. Utiliza la estructura MIENTRAS. 
"""
suma = 0
while suma < 101:
    num = int(input("Ingrese un número: "))
    suma += num
print(f"Ha excedido a  100.\nLa suma de lo acumulado es:  {suma}")