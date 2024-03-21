# Importar flask
from flask import Flask

# Crear una instancia de Flask
app = Flask(__name__)

# Crear una ruta
@app.route('/')
def index():
    return 'Hola mundo! 😎'

# Podemos enviar HTML
@app.route('/html')
def html():
    return '<button>Dame clic!</button>'

# Podemos enviar JSON
@app.route('/usuario')
def usuario():
    return {
        'id': 1,
        'nombre': 'Juan',
        'apellido': 'Pérez',
    }

# Podemos recibir parámetros
@app.route('/cliente/<name>')
def cliente(name):
    return f'<h1>Hola {name}</h1>'

# string, int, float, path, uuid
@app.route('/producto/<int:id>')
def producto(id):
    return f'<h1>Producto {id}</h1>'



if __name__ == '__main__':
    app.run(debug=True)