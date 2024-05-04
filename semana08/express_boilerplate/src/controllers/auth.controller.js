import { prisma } from "../config/prisma.js";
import { CreateUserSchema, LoginSchema } from "../schemas/users.schema.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const signup = async (req, res) => {
  try {
    const { body } = req;
    const validatedBody = CreateUserSchema.parse(body);

    const user = await prisma.user.findFirst({
      where: {
        email: validatedBody.email,
      },
    });

    if (user) {
      throw new Error("User already exists");
    }

    validatedBody.password = await bcrypt.hash(validatedBody.password, 10);

    let newUser = await prisma.user.create({
      data: validatedBody,
    });

    const payload = {
      id: newUser.id,
      email: newUser.email,
      name: newUser.name,
    };
    const secretKey = process.env.SECRET_KEY;
    const access_token = jwt.sign(payload, secretKey, { expiresIn: "7d" });

    return res.status(201).json({
      access_token: access_token,
    });
  } catch (error) {
    return res.status(500).json({
      errors: error.message,
    });
  }
};

export const login = async (req, res) => {
  try {
    const { body } = req;
    const validatedBody = LoginSchema.parse(body);

    const user = await prisma.user.findFirst({
      where: {
        email: validatedBody.email,
      },
    });

    if (!user) {
      throw new Error("Credentials are invalid");
    }

    const isPasswordValid = await bcrypt.compare(
      validatedBody.password,
      user.password
    );

    if (!isPasswordValid) {
      throw new Error("Credentials are invalid");
    }

    const payload = {
      id: user.id,
      email: user.email,
      name: user.name,
    };
    const secretKey = process.env.SECRET_KEY;
    const access_token = jwt.sign(payload, secretKey, { expiresIn: "7d" });

    return res.status(200).json({
      access_token: access_token,
    });
  } catch (error) {
    return res.status(500).json({
      errors: error.message,
    });
  }
};
