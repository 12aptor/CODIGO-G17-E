import { prisma } from "../config/prisma.js";
import { CreateUserSchema } from "../schemas/users.schema.js";
import { ZodError } from "zod";

export const getAllUsers = async (req, res) => {
  try {
    const users = await prisma.user.findMany();

    return res.status(200).json(users);
  } catch (error) {
    return res.status(500).json({
      errors: error.message,
    });
  }
};

export const createUser = async (req, res) => {
  try {
    const { body } = req;
    const validatedBody = CreateUserSchema.parse(body);

    const user = await prisma.user.create({
      data: {
        name: validatedBody.name,
        last_name: validatedBody.last_name,
        email: validatedBody.email,
        password: validatedBody.password,
        role: validatedBody.role,
      },
    });

    return res.status(201).json(user);
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        errors: error.issues,
      });
    }

    return res.status(500).json({
      errors: error.message,
    });
  }
};

export const getUserById = async (req, res) => {
  try {
    const { userId } = req.params;

    const user = await prisma.user.findUnique({
      where: {
        id: parseInt(userId),
      },
    });

    if (!user) {
      throw new Error("User not found");
    }

    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).json({
      errors: error.message,
    });
  }
};

export const updateUser = async (req, res) => {
  try {
    const { userId } = req.params;
    const { body } = req;

    const user = await prisma.user.findUnique({
      where: {
        id: parseInt(userId),
      },
    });

    if (!user) {
      throw new Error("User not found");
    }

    const updatedUser = await prisma.user.update({
      where: {
        id: parseInt(userId),
      },
      data: {
        name: body.name,
        last_name: body.last_name,
        email: body.email,
        password: body.password,
        role: body.role,
      },
    });

    return res.status(200).json(updatedUser);
  } catch (error) {
    return res.status(500).json({
      errors: error.message,
    });
  }
};

export const deleteUser = async (req, res) => {
  try {
    const { userId } = req.params;

    const user = await prisma.user.findUnique({
      where: {
        id: parseInt(userId),
      },
    });

    if (!user) {
      throw new Error("user not found");
    }

    await prisma.user.delete({
      where: {
        id: parseInt(userId),
      },
    });

    return res.status(200).json({ message: "User deleted" });
  } catch (error) {
    return res.status(500).json({
      errors: error.message,
    });
  }
};
