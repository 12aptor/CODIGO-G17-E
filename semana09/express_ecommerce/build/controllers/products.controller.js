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
Object.defineProperty(exports, "__esModule", { value: true });
exports.createProduct = exports.getAllProducts = void 0;
const products_schema_1 = require("../schemas/products.schema");
const zod_1 = require("zod");
const prisma_1 = require("../config/prisma");
const aws_1 = require("../config/aws");
const client_s3_1 = require("@aws-sdk/client-s3");
const s3_request_presigner_1 = require("@aws-sdk/s3-request-presigner");
const getAllProducts = (_req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const products = yield prisma_1.prisma.product.findMany();
        let productsWithSignedUrl = [];
        for (let index = 0; index < products.length; index++) {
            const product = products[index];
            productsWithSignedUrl.push(Object.assign(Object.assign({}, product), { image: yield (0, s3_request_presigner_1.getSignedUrl)(aws_1.s3Client, new client_s3_1.GetObjectCommand({
                    Bucket: "ecommerce-100",
                    Key: product.image,
                })) }));
        }
        return res.status(200).json(productsWithSignedUrl);
    }
    catch (error) {
        if (error instanceof Error) {
            return res.status(500).json({
                errors: error.message,
            });
        }
    }
});
exports.getAllProducts = getAllProducts;
const createProduct = (_req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const { file } = _req;
        if (!file) {
            throw new Error("Image is required");
        }
        const { body } = _req;
        const newBody = {
            name: body.name,
            description: body.description,
            price: parseFloat(body.price),
            stock: parseInt(body.stock),
        };
        const validatedBody = products_schema_1.CreateProductSchema.parse(newBody);
        const s3Response = yield aws_1.s3Client.send(new client_s3_1.PutObjectCommand({
            Bucket: "ecommerce-100",
            Key: file.originalname,
            Body: file.buffer,
        }));
        if (s3Response.$metadata.httpStatusCode !== 200) {
            throw new Error("Error uploading image");
        }
        const product = yield prisma_1.prisma.product.create({
            data: Object.assign(Object.assign({}, validatedBody), { image: file.originalname }),
        });
        return res.status(201).json(product);
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
exports.createProduct = createProduct;
