const sendProduct = async () => {
  const response = await fetch("https://api.example.com/products", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: "product name",
      price: 100,
    }),
  });
};
