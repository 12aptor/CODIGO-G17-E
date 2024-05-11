"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CreateProductSchema = void 0;
const zod_1 = require("zod");
exports.CreateProductSchema = zod_1.z.object({
    name: zod_1.z.string().min(3).max(255),
    description: zod_1.z.string().min(3).max(255),
    price: zod_1.z.number().min(0),
    stock: zod_1.z.number().min(0),
});
