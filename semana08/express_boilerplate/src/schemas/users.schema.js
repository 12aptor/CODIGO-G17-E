import { z } from "zod";

export const CreateUserSchema = z.object({
  name: z.string(),
  last_name: z.string(),
  email: z.string().email(),
  password: z.string(),
  role: z.enum(["ADMIN", "USER"]),
});
