import { Router } from "express";
import * as usersController from "../controllers/users.controller.js";

export const usersRouter = Router();

usersRouter.get("/all", usersController.getAllUsers);
usersRouter.post("/create", usersController.createUser);
usersRouter.get("/by-id/:userId", usersController.getUserById);
usersRouter.put("/update/:userId", usersController.updateUser);
usersRouter.delete("/update/:userId", usersController.deleteUser);
