"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const users_router_1 = require("./routes/users.router");
const auth_router_1 = require("./routes/auth.router");
const app = (0, express_1.default)();
app.use(express_1.default.json());
const port = 3000;
app.use("/api/users", users_router_1.usersRouter);
app.use("/api/auth", auth_router_1.authRouter);
app.listen(port, () => {
    console.log(`Server is running: http://localhost:${port}`);
});
