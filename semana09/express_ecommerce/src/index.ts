import express from "express";
import { usersRouter } from "./routes/users.router";
import { authRouter } from "./routes/auth.router";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());
const port = 3000;

app.use("/api/users", usersRouter);
app.use("/api/auth", authRouter);

app.listen(port, () => {
  console.log(`Server is running: http://localhost:${port}`);
});
