"""Condicionales en Python"""

# Condicionales
# if
# if 10 > 5:
#     print("10 es mayor que 5")

# if else
# if 10 < 5:
#     print("10 es menor que 5")
# else:
#     print("10 no es menor que 5")

# if elif else
# if 10 < 5:
#     print("10 es menor que 5")
# elif 10 == 5:
#     print("10 es igual a 5")
# else:
#     print("10 no es menor que 5 y no es igual a 5")

# Match
x = 20
match x:
    case 10:
        print("x es igual a 10")
    case 20:
        print("x es igual a 20")
    case _:
        print("x no es igual a 10 ni a 20")