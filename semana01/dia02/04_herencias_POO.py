"""Herenicas en POO"""
# Una clase puede heredar de otra clase, es decir, una clase puede
# tomar los atributos y métodos de otra clase.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f'Hola, soy {self.nombre} y tengo {self.edad} años'
    

class Alumno(Persona):
    def hablar(self):
        return self.saludar() + ' y soy un alumno'
    
# persona = Persona('Juan', 25)
# print(persona.saludar())

alumno = Alumno('Pedro', 20)
print(alumno.hablar())