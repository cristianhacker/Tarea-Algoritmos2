"""Desarrolle un algoritmo que simule una alcancía de ahorro. Donde debemos seguir ingresando dinero a la 
alcancía de ahorro hasta que tengamos ahorrado 100 soles. Cuando tengamos ahorrado 100 soles o más indica cuanto
 tienes ahorrado, empezando diciendo “Tienes ahorrado: ”
"""
ahorro = 0
while ahorro <=100:
    user = float(input("Ingrese un monto a ahorrar: "))
    ahorro += user
print(f"Haz superado los 100 soles.\nTienes ahorrado: {ahorro}")