# Entorno virtual

Un entorno virtual es un entorno de Python que permite instalar paquetes de manera aislada.

## Crear un entorno virtual

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