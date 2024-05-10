import express from "express";

const app = express();
app.use(express.json());
app.use(express.json());
const port = 3000;




app.listen(port, () => {
  console.log(`Server is running: http://localhost:${port}`);
});
