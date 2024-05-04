import { Router } from "express";
import * as postsController from "../controllers/posts.controller.js";

export const postsRouter = Router();

postsRouter.get("/all", postsController.getAllPosts);
postsRouter.post("/create", postsController.createPost);
