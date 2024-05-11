// Crear una transacción (tipado con TypeScript)
// Conectarnos con aws y cargar la imagen
// Guardar la información en la base de datos
import { Request, Response } from "express";
import { CreateProductSchema } from "../schemas/products.schema";
import { ZodError } from "zod";
import { prisma } from "../config/prisma";
import { s3Client } from "../config/aws";
import { PutObjectCommand, GetObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

export const getAllProducts = async (_req: Request, res: Response) => {
  try {
    const products = await prisma.product.findMany();

    let productsWithSignedUrl = [];
    for (let index = 0; index < products.length; index++) {
      const product = products[index];

      productsWithSignedUrl.push({
        ...product,
        image: await getSignedUrl(
          s3Client,
          new GetObjectCommand({
            Bucket: "ecommerce-100",
            Key: product.image,
          })
        ),
      });
    }

    return res.status(200).json(productsWithSignedUrl);
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        errors: error.message,
      });
    }
  }
};

export const createProduct = async (_req: Request, res: Response) => {
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

    const validatedBody = CreateProductSchema.parse(newBody);

    const s3Response = await s3Client.send(
      new PutObjectCommand({
        Bucket: "ecommerce-100",
        Key: file.originalname,
        Body: file.buffer,
      })
    );

    if (s3Response.$metadata.httpStatusCode !== 200) {
      throw new Error("Error uploading image");
    }

    const product = await prisma.product.create({
      data: {
        ...validatedBody,
        image: file.originalname,
      },
    });

    return res.status(201).json(product);
  } catch (error) {
    if (error instanceof ZodError) {
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
};
