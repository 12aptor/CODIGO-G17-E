const API_URL = "http://localhost:3000";
const socket = io(API_URL);

const username = document.getElementById("username");
const generalRoom = document.getElementById("generalRoom");
const randomRoom = document.getElementById("randomRoom");
const inputMessage = document.getElementById("inputMessage");
const chat = document.getElementById("chat");
const room = document.getElementById("room");
const rooms = document.getElementById("rooms");
const messagesList = document.getElementById("messagesList");

let roomName = "";
const joinRoom = async (selectedRoom) => {
  const prevMessages = await fetch(
    "http://localhost:3000/messages/" + selectedRoom
  );

  if (!prevMessages.ok) {
    alert("Error al obtener los mensajes");
    return;
  }

  const prevMessagesJson = await prevMessages.json();

  for (let index = 0; index < prevMessagesJson.length; index++) {
    const _message = prevMessagesJson[index];
    const li = document.createElement("li");
    li.textContent = `${_message.username}: ${_message.message}`;
    messagesList.appendChild(li);
  }

  const usernameValue = username.value;
  if (usernameValue.trim() === "") {
    alert("Por favor, ingrese un nombre de usuario");
    return;
  }

  socket.emit("join", selectedRoom);
  rooms.style.display = "none";
  room.style.display = "block";
  roomName = selectedRoom;
};

generalRoom.addEventListener("click", () => {
  joinRoom("generalRoom");
});

randomRoom.addEventListener("click", () => {
  joinRoom("randomRoom");
});

chat.addEventListener("submit", (e) => {
  e.preventDefault();
  const message = inputMessage.value;

  if (message.trim() !== "") {
    socket.emit("chat", {
      message: message,
      room: roomName,
      username: username.value,
    });
  }
});

socket.on("chat", (message) => {
  const li = document.createElement("li");
  li.textContent = `${message.username}: ${message.message}`;
  messagesList.appendChild(li);
  inputMessage.value = "";
});
