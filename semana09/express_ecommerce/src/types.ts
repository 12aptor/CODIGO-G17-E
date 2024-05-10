import { Roles } from "@prisma/client";

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
  errors: string;
}
