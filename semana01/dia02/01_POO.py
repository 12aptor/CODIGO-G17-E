"""Objetos y Clases"""

class Vehiculo:
    # Métodos mágicos
    def __init__(self, co, ma, mo, pr) -> None:
        # Atributos
        self.color = co
        self.marca = ma
        self.modelo = mo
        self.precio = pr

    # Métodos
    def mostrar_info(self):
        return f"Color: {self.color} y Marca: {self.marca}"
    
    # Métodos mágicos: Representación de un objeto con un string
    def __str__(self):
        return f"Marca: {self.marca}"
    
    # Métodos privados: Solo se pueden acceder desde la misma clase
    def __metodo_privado(self):
        return "Método privado"

# Instanciar un objeto
mercedez = Vehiculo("Rojo", "Mercedez", "2020", 1000000)
# print(mercedez.color)
# print(mercedez.mostrar_info())
# print(mercedez)
print(mercedez.__metodo_privado())