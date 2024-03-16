"""Crear un objeto llamado Rectangulo con atributos base y altura,
y métodos para calcular el área. Instanciar el objeto y mostrar el área."""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    

rectangulo = Rectangulo(10, 5)
print(rectangulo.calcular_area())