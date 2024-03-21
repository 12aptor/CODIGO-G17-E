# Importar flask
from flask import Flask

# Crear una instancia de Flask
app = Flask(__name__)

# Crear una ruta
@app.route('/')
def index():
    return 'Hola mundo! 😎'

if __name__ == '__main__':
    app.run(debug=True)