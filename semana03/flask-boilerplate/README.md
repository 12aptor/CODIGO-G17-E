# Creación de un proyecto de Flask

## Creación de un entorno virtual (entorno_flask_boilerplate)

```bash
# Mac/Linux
python3 -m venv nombre_entorno

# Windows
python -m venv nombre_entorno
```

## Activación del entorno virtual

```bash
# Mac/Linux
source nombre_entorno/bin/activate

# Windows
nombre_entorno\Scripts\activate

# Git Bash
source nombre_entorno/Scripts/activate
```

## Instalación de Flask

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install psycopg2-binary
```


## Creación de la aplicación

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running! 🤠'

if __name__ == '__main__':
    app.run(debug=True)
```


## Ejecución de la aplicación

```bash
python app.py
```

## Migramos la base de datos

```bash
# Inicializamos la base de datos (solo la primera vez)
flask db init

# Creamos la migración
flask db migrate -m "Un mensaje"

# Aplicamos la migración
flask db upgrade
```

## Creación del flujo de trabajo

- Crear los modelos (contiene la estructura de la base de datos)
- Crear los controladores (contiene toda la lógica de la aplicación)
- Crear las rutas (contiene las rutas de la aplicación)