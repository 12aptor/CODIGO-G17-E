import { Router } from "express";
import * as productsController from "../controllers/products.controller.js";

export const productsRouter = Router();

productsRouter.post("/create", productsController.createProduct);
productsRouter.get("/all", productsController.getAllProducts);
