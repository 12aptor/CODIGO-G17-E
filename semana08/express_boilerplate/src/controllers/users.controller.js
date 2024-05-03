import { prisma } from "../config/prisma.js";

export const getAllUsers = async (req, res) => {
  const users = await prisma.user.findMany();

  console.log(users);

  return res.json({ ok: true });
};
