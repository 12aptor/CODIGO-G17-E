"""Diccionarios en python"""

# Un diccionario es una estructura de datos que permite almacenar pares de valores
# clave-valor. Es decir, a cada valor almacenado se le asocia una clave que lo
# identifica. Los diccionarios son mutables, es decir, pueden ser modificados

usuario = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juan@gmail.com",
    "skills": ["python", "java", "c++"]
}

# Acceder a un valor
print(usuario["nombre"])

# Modificar un valor
usuario["nombre"] = "Juanito"

# Agregar un nuevo valor
usuario["edad"] = 30

# Eliminar un valor
del usuario["email"]

print(usuario)