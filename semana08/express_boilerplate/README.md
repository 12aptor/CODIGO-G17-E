# Express

## Crear un proyecto de Express

1. Crear un directorio para el proyecto
2. Inicializar el proyecto con npm
3. Instalar express

### Crear un directorio para el proyecto

```bash
mkdir myapp
cd myapp
```

### Inicializar el proyecto con npm

```bash
npm init
# ó
npm init -y
```

### Instalar express

```bash
npm install express
```

### Crear un archivo de entrada `index.js`

```javascript
import express from "express";

const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(port, () => {
  console.log(`El servidor está corriendo en: http://localhost:${port}`);
});
```

### Agregar type module en el package.json

```json
{
    ...
    "type": "module"
    ...
}
```

### Ejecutar el servidor

```bash
node index.js
```

### Para el hot reload

```bash
npm install -D nodemon
```

### Instalar PrismaORM

```bash
npm install prisma
```

### Inicializar PrismaORM

```bash
npx prisma init
```

### Ejecutar las migraciones

```bash
npx prisma migrate dev
```

### Instalar @prisma/client

```bash
npm install @prisma/client
```