# Docker

## Dockerfile

```dockerfile
FROM node:20.3.0

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install

# Copiar todo el contenido de la carpeta actual a la carpeta de trabajo
COPY . .

# Exponer el puerto 3000
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["npm", "start"]
```

## Comandos

### Crear una imagen

```bash
docker build -t nombre-imagen .
```

## Correr un contenedor

```bash
docker run -p 3000:3000 nombre-imagen
```

## Ver contenedores en ejecución

```bash
docker ps
```

## Ver todos los contenedores

```bash
docker ps -a
```

## Detener un contenedor

```bash
docker stop id-contenedor
```

## Eliminar un contenedor

```bash
docker rm id-contenedor
```

## Eliminar una imagen

```bash
docker rmi nombre-imagen
```

## Ver las imágenes

```bash
docker images
```

## Ver logs de un contenedor

```bash
docker logs id-contenedor
```