import { z } from "zod";

export const CreateSaleSchema = z.object({
  total: z.number().positive(),
  user_id: z.number().positive(),
  details: z.array(
    z.object({
      quantity: z.number().positive(),
      price: z.number().positive(),
      total: z.number().positive(),
      product_id: z.number().positive(),
    })
  ),
});
