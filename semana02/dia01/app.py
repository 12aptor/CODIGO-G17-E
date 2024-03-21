# Importar flask
from flask import Flask, render_template, request

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

# Métodos HTTP (GET, POST, PUT, DELETE, PATCH, OPTIONS)
@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    return 'Hola mundo! 😄'

# Plantillas (tener una carpeta templates)
@app.route('/template')
def template():
    username = 'Pepito'
    return render_template('index.html', username= username)

@app.route('/login', methods=['POST'])
def login():
    # Recuperar la ruta
    path = request.path
    print(path)

    # Recuperar el método
    method = request.method
    print(method)

    # Recuperar archivos
    # file = request.files['foto']
    # print(file)

    # Recuperar datos del formdata
    # name = request.form['nombre']
    # print(name)

    # Recuperar el body
    json = request.get_json()
    return json, 200

if __name__ == '__main__':
    app.run(debug=True)