const API_URL = "http://localhost:3000";
const socket = io(API_URL);

const username = document.getElementById("username");
const generalRoom = document.getElementById("generalRoom");
const randomRoom = document.getElementById("randomRoom");
const inputMessage = document.getElementById("inputMessage");
const chat = document.getElementById("chat");
const room = document.getElementById("room");
const rooms = document.getElementById("rooms");

let roomName = "";
const joinRoom = (selectedRoom) => {
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
      message,
      user: username.value,
      room: roomName,
    });
  }
});

socket.on("chat", (message) => {
  const messagesList = document.getElementById("messagesList");
  const li = document.createElement("li");
  li.textContent = `${message.user}: ${message.message}`;
  messagesList.appendChild(li);
  inputMessage.value = "";
});
