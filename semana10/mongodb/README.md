# MongoDB

## Abrir terminal de MongoDB

```bash
mongosh
```

## Crear base de datos `test`

```bash
use test
```

## Crear colección `users`

```javascript
db.createCollection("users");
// ó
db.users.insertOne({ name: "John Doe", age: 30 });
```

## Insertar documentos en la colección `users`

```javascript
db.users.insertOne({ name: "Jane Doe", age: 25 });
// ó
db.users.insertMany([
  { name: "John Doe", age: 30 },
  { name: "Jane Doe", age: 25 },
  { name: "Alice Doe", age: 35 },
  { name: "Bob Doe", age: 40 },
  { name: "Charlie Doe", age: 45 },
  { name: "David Doe", age: 50 }
]);
```

## Listar colecciones

```javascript
show collections
```

## Listar documentos de la colección `users`

```javascript
db.users.find();
```

## Filtrar documentos de la colección `users`

```javascript
db.users.find({ name: "John Doe" });
db.users.find({ age: { $gt: 25 } });
```

## Actualizar documentos de la colección `users`

```javascript
db.users.updateOne({ name: "John Doe" }, { $set: { age: 35 } });
// ó
db.users.updateMany({ age: { $lt: 30 } }, { $set: { age: 30 } });
// ó
db.users.updateMany({}, {
    $set: {
        status: true
    }
});
```

## Eliminar documentos de la colección `users`

```javascript
db.users.deleteOne({ name: "John Doe" });
// ó
db.users.deleteMany({ age: { $lt: 30 } });
db.users.deleteMany({});
```

## 