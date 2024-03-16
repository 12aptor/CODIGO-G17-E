"""Bucles en python"""

# Bucle while
# Ejemplo 1
i = 1

while i < 6:
    print(i)
    i += 1

# Bucle for
# Ejemplo 1
frutas = ["manzana", "pera", "uva"]

for x in frutas:
    print(x)

# continue: Salta a la siguiente iteración
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        continue
    print(numero)

# break: Termina el bucle
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        break
    print(numero)