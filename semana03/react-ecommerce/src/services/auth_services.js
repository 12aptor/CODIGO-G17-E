import { API_URL } from "../helpers/constants";

export const postLogin = async (credentials) => {
  try {
    const response = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(credentials),
    });

    if (!response.ok) {
      return null;
    }

    return response.json();
  } catch (error) {
    return null;
  }
};

export const isAuthenticated = () => {
  const token = localStorage.getItem("token");

  if (!token) {
    return false;
  }

  const [, payload] = token.split(".");
  const payloadDecoded = atob(payload);
  const payloadJSON = JSON.parse(payloadDecoded);

  if (payloadJSON.exp < Date.now() / 1000) {
    return false;
  }

  return true;
};
