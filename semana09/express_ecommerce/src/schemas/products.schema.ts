import { z } from "zod";

export const CreateProductSchema = z.object({
  name: z.string().min(3).max(255),
  description: z.string().min(3).max(255),
  price: z.number().min(0),
  stock: z.number().min(0),
});
