import { Router } from "express";
import * as salesController from "../controllers/sales.controller";

export const salesRouter = Router();

salesRouter.post("/create", salesController.createSale);
