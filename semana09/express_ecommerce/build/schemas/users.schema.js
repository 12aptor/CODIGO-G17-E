"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.LoginSchema = exports.UpdateUserSchema = exports.CreateUserSchema = void 0;
const zod_1 = require("zod");
exports.CreateUserSchema = zod_1.z.object({
    name: zod_1.z.string(),
    last_name: zod_1.z.string(),
    email: zod_1.z.string().email(),
    password: zod_1.z.string(),
    role: zod_1.z.enum(["CLIENT", "USER"]),
});
exports.UpdateUserSchema = zod_1.z.object({
    name: zod_1.z.string().optional(),
    last_name: zod_1.z.string().optional(),
    email: zod_1.z.string().email().optional(),
    password: zod_1.z.string().optional(),
    role: zod_1.z.enum(["CLIENT", "USER"]).optional(),
});
exports.LoginSchema = zod_1.z.object({
    email: zod_1.z.string().email(),
    password: zod_1.z.string(),
});
