import { Request, Response } from "express";
import { ZodError } from "zod";
import { CreateSaleSchema } from "../schemas/sales.schema";
import { prisma } from "../config/prisma";

export const createSale = async (_req: Request, res: Response) => {
  try {
    const { body } = _req;
    const validatedBody = CreateSaleSchema.parse(body);

    let sale;
    await prisma.$transaction(async (tx) => {
      sale = await tx.sale.create({
        data: {
          total: validatedBody.total,
          user_id: validatedBody.user_id,
          saleDetail: {
            create: validatedBody.details,
          },
        },
      });

      for (let index = 0; index < validatedBody.details.length; index++) {
        const detail = validatedBody.details[index];

        await tx.product.update({
          where: {
            id: detail.product_id,
          },
          data: {
            stock: {
              decrement: detail.quantity,
            },
          },
        });
      }
    });

    return res.status(201).json(sale);
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        errors: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        errors: error.message,
      });
    }
  }
};
