"""Desarrolle un algoritmo en Pseudocódigo y programa en Python, donde pida ingresar la operación a calcular.
Las opciones válidas son “S”, “R”, “M”. En caso de ingresar otra letra debe de volver a preguntar
 hasta que ingrese una opción válida.
Además, debe ingresar cantidad de números y luego debe ingresar los valores de estos números uno por uno. 
Si la operación ingresada es “S”, debemos realizar la suma de todos los números ingresados
Si la operación ingresada es “R”, debemos realizar la resta de todos los números
Si la operación ingresada es “M”, debemos realizar la multiplicación de todos los números
"""
print("S = Suma\nR = Resta\nM = Multiplicación")
while True:
        oper = input("Seleccione una opción: ").upper()
        if oper in ["S" , "R", "M"]:
            break
        else:
            print("Escoja una opcion válida")


cant = int(input("Ingrese una cantidad de números: "))
lista = []

for i in range(cant):
     num = int(input("Ingrese un número: "))
     lista.append(num)

if oper == "S":
     resultado = 0
     for s in lista:
          resultado += s
elif oper == "R":
     resultado = lista[0]
     for r in lista[1:]:
          resultado -= r
else:
     resultado = 1 
     for m in lista:
          resultado *= m

          

print(f"La lista de números es: {lista}")    
print(f"EL resultado de {oper} es: {resultado}")
    

    
     
     
    

     
   
