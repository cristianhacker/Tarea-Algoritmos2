"""Elabora un programa que genere la siguiente serie: 30 27 24 …… 12
Además, debe mostrar la cantidad de números que se encuentran en dicho rango
"""
cant = 0
for i in range(30,11,-3):
    cant += 1
    print(i, end=",")
print(f"\nLos números del 30 al 12 en -3 es : {cant}")


