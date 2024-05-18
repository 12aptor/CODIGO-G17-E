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