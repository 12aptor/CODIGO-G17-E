import express from "express";
import { productsRouter } from "./routes/products.router.js";

const app = express();
app.use(express.json());
const port = 3000;

app.use("/api/products", productsRouter);

app.listen(port, () => {
  console.log(`El servidor está corriendo en: http://localhost:${port}`);
});
