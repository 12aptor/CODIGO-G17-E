import { useEffect, useState } from "react";
import { getProductsServices } from "../../services/products_services";
import { Link } from "react-router-dom";

export const Home = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProductsServices().then((data) => {
      if (!data) {
        alert("Ha ocurrido un error");
        return;
      }

      setProducts(data);
    });
  }, []);

  const handleAddToCart = (product) => {
    const cart = localStorage.getItem("cart") || "[]";
    const cartParsed = JSON.parse(cart);
    const productInCart = cartParsed.find((item) => item.id === product.id);

    if (productInCart) {
      // Incrementamos la cantidad del producto en el carrito
      const newCart = cartParsed.map((item) => {
        if (item.id === product.id) {
          return {
            ...item,
            quantity: item.quantity + 1,
            subtotal: parseFloat(item.subtotal) + parseFloat(item.price),
          };
        }
        return item;
      });

      localStorage.setItem("cart", JSON.stringify(newCart));
      return;
    }
    // Agregamos el producto al carrito
    const newProduct = {
      ...product,
      quantity: 1,
      subtotal: parseFloat(product.price),
    };

    localStorage.setItem("cart", JSON.stringify([...cartParsed, newProduct]));
  };

  return (
    <div>
      <div className="flex justify-between">
        <h1>Productos</h1>
        <Link
          to="cart"
          className="px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm text-gray-900"
        >
          Carrito de compras
        </Link>
      </div>
      <div className="flex gap-5 flex-wrap">
        {products.length > 0 ? (
          products.map((product, index) => (
            <div key={index} className="min-w-96">
              <picture className="block rounded-lg overflow-hidden aspect-video relative">
                <img
                  src={product.image}
                  alt="Product image"
                  className="w-full"
                />
              </picture>
              <div className="pt-5">
                <h2>{product.name}</h2>
                <p>{product.description}</p>
                <p>{product.price}</p>
                <button
                  type="button"
                  className="px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm text-gray-900"
                  onClick={() => handleAddToCart(product)}
                >
                  Añadir a carrito
                </button>
              </div>
            </div>
          ))
        ) : (
          <p>No hay productos</p>
        )}
      </div>
    </div>
  );
};
