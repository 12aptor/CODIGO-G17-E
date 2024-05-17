import express from "express";
import http from "http";
import { Server } from "socket.io";
import { testDb } from "./mongo.js";

const app = express();
const port = process.env.PORT || 3000;
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    // origin: "*",
    origin: "http://127.0.0.1:5500",
  },
});

app.get("/", async (req, res) => {
  return res.send("Hello World");
});

app.get("/messages/:room", async (req, res) => {
  try {
    const room = req.params.room;

    const collection = await testDb.collection("messages");
    const messages = await collection
      .find({
        room: room,
      })
      .toArray();

    return res.status(200).json(messages);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

io.on("connection", (socket) => {
  socket.on("join", (room) => {
    console.log("Usuario conectado a la sala: ", room);
    socket.join(room);
  });

  socket.on("chat", (message) => {
    // io.emit("chat", message);
    io.to(message.room).emit("chat", message);
  });

  socket.on("disconnect", () => {
    console.log("Usuario desconectado");
  });
});

server.listen(port, () => {
  console.log(`Running: http://localhost:${port}`);
});
