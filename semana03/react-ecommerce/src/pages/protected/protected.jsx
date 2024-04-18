export const Protected = () => {
  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <div>
      <h1>Esta ruta está protegida</h1>
      <p>Hola mundo</p>
      <button type="button" onClick={handleLogout}>
        Cerrar sesión
      </button>
    </div>
  );
};
