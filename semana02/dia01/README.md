# Flask

Flask es un microframework para Python que permite crear aplicaciones web de manera sencilla.

## Creación de un entorno virtual

```bash
# Mac y Linux
python3 -m venv nombre_del_entorno

# Windows
python -m venv nombre_del_entorno
```

## Activar un entorno virtual

```bash
# Mac y Linux
source nombre_del_entorno/bin/activate

# Windows cmd
nombre_del_entorno\Scripts\activate
# Git Bash
source nombre_del_entorno/Scripts/activate
```

## Desactivar un entorno virtual

```bash
deactivate
```

## Instalación

```bash
pip install Flask
```

## Creación de una aplicación

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo! 😎'
```

## Ejecución de la aplicación

```bash
flask run
```

## Crear nuestro requirements.txt

```bash
pip freeze > requirements.txt
```

## Crear el archivo runtime.txt

```bash 
python-3.8.5
```