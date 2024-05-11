import { Router } from "express";
import * as productsController from "../controllers/products.controller";
import multer from "multer";

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

export const productsRouter = Router();

productsRouter.post(
  "/create",
  upload.single("image"),
  productsController.createProduct
);
