import { Router } from "express";
import * as usersController from "../controllers/users.controller.js";

export const usersRouter = Router();

usersRouter.get("/all", usersController.getAllUsers);
