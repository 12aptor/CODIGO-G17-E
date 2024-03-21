-- Crear una base de datos postgresql
CREATE DATABASE "flask";

-- Crear una tabla con postgresql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
)