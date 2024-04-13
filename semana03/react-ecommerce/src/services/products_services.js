import { API_URL } from "../helpers/constants";

export const getProductsServices = async () => {
  try {
    const response = await fetch(`${API_URL}/products/all`);

    if (!response.ok) {
      return null;
    }

    return response.json();
  } catch (error) {
    return null;
  }
};
