import { useState } from "react";

export const Cart = () => {
  const [cart, setCart] = useState(
    JSON.parse(localStorage.getItem("cart")) || []
  );

  const handleDeleteItem = (id) => {
    const newCart = cart.filter((item) => item.id !== id);

    setCart(newCart);
    localStorage.setItem("cart", JSON.stringify(newCart));
  };

  return (
    <div>
      <h1>Carrito</h1>
      <table>
        <thead>
          <tr>
            <th>Producto</th>
            <th>Cantidad</th>
            <th>Precio</th>
            <th>Subtotal</th>
            <th>Accciones</th>
          </tr>
        </thead>
        <tbody>
          {cart.length > 0 ? (
            cart.map((item, index) => (
              <tr key={index}>
                <td>{item.name}</td>
                <td>{item.quantity}</td>
                <td>{item.price}</td>
                <td>{item.subtotal}</td>
                <td>
                  <button
                    type="button"
                    className="p-3 bg-white text-gray-900"
                    onClick={() => handleDeleteItem(item.id)}
                  >
                    X
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td>Carrito sin productos</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};
