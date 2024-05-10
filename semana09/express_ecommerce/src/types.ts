import { Roles } from "@prisma/client";
import { ZodIssue } from "zod";

export interface IPayload {
  id: number;
  name: string;
  email: string;
  role: Roles;
}

export interface ISignupResponse {
  access_token: string;
}

export interface IErrorResponse {
  errors: string | ZodIssue[];
}
