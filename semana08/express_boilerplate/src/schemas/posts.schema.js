import { z } from "zod";

export const CreatePostSchema = z.object({
  title: z.string().min(5).max(255),
  content: z.string().min(5),
  user_id: z.number().int(),
});
