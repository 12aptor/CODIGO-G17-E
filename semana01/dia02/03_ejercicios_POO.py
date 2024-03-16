"""Crear un objeto llamado Usuario con los siguientes atributos:
- Nombre
- Apellido
- Email
- Password
Con los siguientes métodos:
- Saludar: que imprima "Hola, soy {Nombre} {Apellido}"
- Encriptar Password: que encripte el password y lo retorne
- Mostrar info: que retorne todos los atributos en un diccionario"""
import hashlib
from pprint import pprint

class Usuario:
    def __init__(self, nombre: str, apellido: str, email: str, password: str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = self.__encriptar_password(password)

    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellido}"
    
    def __encriptar_password(self, password):
        sha256 = hashlib.sha256()
        pwd_bytes = password.encode('utf-8')
        sha256.update(pwd_bytes)
        pwd_hash = sha256.hexdigest()
        return pwd_hash
    
    def mostrar_info(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password': self.password
        }

usuario = Usuario("Eduardo", "De Rivero", "eduardo@gmail.com", "osito123")
print(usuario.saludar())
pprint(usuario.mostrar_info())