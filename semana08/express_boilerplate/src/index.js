import express from "express";
import { productsRouter } from "./routes/products.router.js";
import { usersRouter } from "./routes/users.router.js";
import { authMiddleware } from "./middlewares/auth.middleware.js";
import cors from "cors";
import morgan from "morgan";

const app = express();
app.use(cors());
app.use(morgan("dev"));
app.use(express.json());
const port = 3000;

app.use("/api/products", authMiddleware, productsRouter);
app.use("/api/users", usersRouter);

app.listen(port, () => {
  console.log(`El servidor está corriendo en: http://localhost:${port}`);
});
