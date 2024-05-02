export const createProduct = (req, res) => {
  const { body } = req;

  return res.json(body);
};

export const getAllProducts = (req, res) => {
  const { name, price } = req.query;

  if (name) {
    console.log(name);
  }

  if (price) {
    const priceFloat = parseFloat(price);
    console.log(typeof priceFloat);
  }

  return res.json([
    {
      id: 1,
      name: "Producto 1",
    },
    {
      id: 2,
      name: "Producto 2",
    },
  ]);
};

export const getProductById = (req, res) => {
  const { id } = req.params;

  return res.json({
    id: parseInt(id),
    name: `Producto ${id}`,
  });
};
