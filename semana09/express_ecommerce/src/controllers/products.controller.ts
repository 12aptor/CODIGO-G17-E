// Crear una transacción (tipado con TypeScript)
// Conectarnos con aws y cargar la imagen
// Guardar la información en la base de datos
import { Request, Response } from "express";

export const createProduct = async (_req: Request, res: Response) => {
  try {
    const { file } = _req;
    console.log(file);
    const { body } = _req;
    console.log(body);

    return res.status(201).json({ ok: true });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        errors: error.message,
      });
    }
  }
};
