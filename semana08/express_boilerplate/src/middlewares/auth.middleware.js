import jwt from "jsonwebtoken";

export const authMiddleware = async (req, res, next) => {
  try {
    const { authorization } = req.headers;

    if (!authorization) {
      return res.status(401).json({ errors: "Unauthorized" });
    }

    const token = authorization.split(" ")[1];

    jwt.verify(token, process.env.SECRET_KEY);

    return next();
  } catch {
    return res.status(401).json({ errors: "Unauthorized" });
  }
};

export const adminMiddleware = async (req, res, next) => {
  try {
    const { authorization } = req.headers;

    if (!authorization) {
      return res.status(401).json({ errors: "Unauthorized" });
    }

    const token = authorization.split(" ")[1];
    const decoded = jwt.verify(token, process.env.SECRET_KEY);

    if (decoded.role !== "ADMIN") {
      return res.status(401).json({ errors: "Unauthorized" });
    }

    return next();
  } catch {
    return res.status(401).json({ errors: "Unauthorized" });
  }
};
