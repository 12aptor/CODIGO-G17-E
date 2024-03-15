lista = ["Juan", "Pedro", "Luis", "Ana", "Maria"]
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaBooleanos = [True, False, True, False, True, False]
listaCombinada = ["Juan", 1, True, "Pedro", 2, False]

"""Métodos de las listas"""
# Agregar elementos a la lista
lista.append("Carlos")
# Agregar elementos en una posición específica
lista.insert(1, "Roberto")
# Eliminar elementos de la lista
lista.remove("Ana")
# Eliminar el último elemento de la lista
lista.pop()
# Eliminar un elemento en una posición específica
lista.pop(2)
# Ordenar la lista
lista.sort()
lista.sort(reverse=True)
# Invertir la lista
lista.reverse()
# Contar elementos de la lista
print(lista.count("Juan"))
# Obtener la posición de un elemento
print(lista.index("Pedro"))
# Obtener la longitud de la lista
print(len(lista))
# Obtener el máximo valor de la lista
print(max(listaNumeros))
# Obtener el mínimo valor de la lista
print(min(listaNumeros))



tupla = ("Juan", "Pedro", "Luis", "Ana", "Maria")
tuplaNumeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuplaBooleanos = (True, False, True, False, True, False)
tuplaCombinada = ("Juan", 1, True, "Pedro", 2, False)