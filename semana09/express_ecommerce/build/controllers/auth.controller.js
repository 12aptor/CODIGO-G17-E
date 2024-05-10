"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.login = exports.signup = void 0;
const prisma_1 = require("../config/prisma");
const users_schema_1 = require("../schemas/users.schema");
const bcrypt_1 = __importDefault(require("bcrypt"));
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const zod_1 = require("zod");
const signup = (_req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const { body } = _req;
        const validatedBody = users_schema_1.CreateUserSchema.parse(body);
        const user = yield prisma_1.prisma.user.findFirst({
            where: {
                email: validatedBody.email,
            },
        });
        if (user) {
            throw new Error("User already exists");
        }
        validatedBody.password = yield bcrypt_1.default.hash(validatedBody.password, 10);
        const newUser = yield prisma_1.prisma.user.create({
            data: validatedBody,
        });
        const payload = {
            id: newUser.id,
            name: newUser.name,
            email: newUser.email,
            role: newUser.role,
        };
        const secretKey = process.env.SECRET_KEY;
        if (!secretKey) {
            throw new Error("Secret key not found");
        }
        const accessToken = jsonwebtoken_1.default.sign(payload, secretKey, { expiresIn: "7d" });
        return res.status(201).json({
            access_token: accessToken,
        });
    }
    catch (error) {
        if (error instanceof zod_1.ZodError) {
            return res.status(400).json({
                errors: error.issues,
            });
        }
        if (error instanceof Error) {
            return res.status(500).json({
                errors: error.message,
            });
        }
    }
});
exports.signup = signup;
const login = (_req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const { body } = _req;
        const validatedBody = users_schema_1.LoginSchema.parse(body);
        const user = yield prisma_1.prisma.user.findFirst({
            where: {
                email: validatedBody.email,
            },
        });
        if (!user) {
            throw new Error("Credentials are invalid");
        }
        const isPasswordValid = bcrypt_1.default.compare(validatedBody.password, user.password);
        if (!isPasswordValid) {
            throw new Error("Credentials are invalid");
        }
        const payload = {
            id: user.id,
            name: user.name,
            email: user.email,
            role: user.role,
        };
        const secretKey = process.env.SECRET_KEY;
        if (!secretKey) {
            throw new Error("Secret key not found");
        }
        const accessToken = jsonwebtoken_1.default.sign(payload, secretKey, { expiresIn: "7d" });
        return res.status(200).json({
            access_token: accessToken,
        });
    }
    catch (error) {
        if (error instanceof zod_1.ZodError) {
            return res.status(400).json({
                errors: error.issues,
            });
        }
        if (error instanceof Error) {
            return res.status(500).json({
                errors: error.message,
            });
        }
    }
});
exports.login = login;
