x = 10
y = 0

# Dentro del bloque try se coloca el código que se quiere ejecutar
# y que puede lanzar una excepción.
try:
    result = x / y

# Dentro del bloque except se coloca el código que se ejecutará
# si se lanza una excepción.
except ZeroDivisionError as e:
    print(e)

# Dentro del bloque finally se coloca el código que se ejecutará
# siempre, independientemente de si se lanza una excepción o no.
finally:
    print("Siempre se ejecuta")


edad = 15
try:
    # Lanzar una excepción: raise
    if edad < 18:
        raise Exception("No puedes pasar")
except Exception as e:
    print(e)