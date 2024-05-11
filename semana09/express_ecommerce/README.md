# Express con typescript

## Instalación

```bash
npm init -y
npm install express
npm install -D @types/express
npm install -D typescript
npm install -D ts-node-dev
npm install cors
npm install -D @types/cors
npm install multer
npm install -D @types/multer
npm install @aws-sdk/client-s3
npm install @aws-sdk/s3-request-presigner
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
