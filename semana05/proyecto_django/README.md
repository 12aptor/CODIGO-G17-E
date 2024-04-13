# Django

## Instalar Django
```bash
pip install django
```

## Crear el proyecto
```bash
django-admin startproject nombre_proyecto
django-admin startproject nombre_proyecto .
```

## Correr el servidor
```bash
python manage.py runserver
```

## Ejecutar las primeras migraciones
```bash
python manage.py migrate
```

## Crear un superusuario
```bash
python manage.py createsuperuser
```

## Crear una aplicación
```bash
python manage.py startapp ecommerce
```

## Registrar la aplicación
```python
INSTALLED_APPS = [
    ...
    'ecommerce',
    ...
]
```

## Migraciones de la aplicación
```bash
python manage.py makemigrations nombre_app
python manage.py migrate

# Verificar las migraciones
python manage.py showmigrations
```

## Consultar datos en la terminal
```bash
python manage.py shell
```