# Express con typescript

## Instalación

```bash
npm init -y
npm install express
npm install -D @types/express
npm install -D typescript
npm install -D ts-node-dev
```

## Agregamos tsc al package.json

```json
"scripts": {
    "dev": "ts-node-dev src/index.ts",
    "tsc": "tsc"
  },
```

## Creamos el archivo tsconfig.json

```bash
npm run tsc -- --init
```
