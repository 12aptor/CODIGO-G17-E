import { useState } from "react";
import { postLogin } from "../../services/auth_services";

export const Login = () => {
  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.currentTarget;
    setCredentials({
      ...credentials,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    postLogin(credentials).then((response) => {
      if (!response) {
        alert("Usuario o contraseña incorrectos");
        return;
      }

      localStorage.setItem("token", response.access_token);
    });
  };

  return (
    <div>
      <form className="max-w-96" onSubmit={handleSubmit}>
        <h1>Ingrese sus credenciales</h1>
        <div className="flex flex-col gap-2">
          <label htmlFor="email">Correo</label>
          <input
            type="text"
            name="email"
            id="email"
            className="w-full"
            onChange={handleInputChange}
          />
        </div>
        <div className="flex flex-col gap-2">
          <label htmlFor="password">Contraseña</label>
          <input
            type="password"
            name="password"
            id="password"
            className="w-full"
            onChange={handleInputChange}
          />
        </div>
        <div className="pt-4">
          <button
            type="submit"
            className="
                px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm text-gray-900
            "
          >
            Iniciar sesión
          </button>
        </div>
      </form>
    </div>
  );
};
