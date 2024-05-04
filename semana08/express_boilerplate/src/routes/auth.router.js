import { Router } from "express";
import * as authController from "../controllers/auth.controller.js";

export const authRouter = Router();

authRouter.post("/signup", authController.signup);
authRouter.post("/login", authController.login);