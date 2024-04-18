import { Navigate } from "react-router-dom";
import { isAuthenticated } from "../../services/auth_services";

export const Protected = () => {
  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  if (!isAuthenticated()) {
    return <Navigate to={"/login"} />;
  }

  return (
    <div>
      <h1>Esta ruta está protegida</h1>
      <p>Hola mundo</p>
      <button
        type="button"
        className="px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm text-gray-900"
        onClick={handleLogout}
      >
        Cerrar sesión
      </button>
    </div>
  );
};
