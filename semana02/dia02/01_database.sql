-- Crear una base de datos postgresql
CREATE DATABASE "flask";

-- Crear una tabla con postgresql
CREATE TABLE IF NOT EXISTS public.usuarios (
	id SERIAL PRIMARY KEY,
	nombres VARCHAR(100),
	apellidos VARCHAR(100),
	edad INTEGER,
	correo VARCHAR(200),
	password TEXT,
	status BOOLEAN,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos en la tabla (podemos insertar uno o varios registros)
INSERT INTO public.usuarios (nombres, apellidos, edad, correo, password, status)
VALUES
	('Miguel', 'Ramirez', 25, 'juan@gmail.com', 'osito123', TRUE),
	('María', 'García', 30, 'maria@gmail.com', 'maria123', FALSE),
	('Carlos', 'López', 35, 'carlos@gmail.com', 'carlos456', TRUE),
	('Laura', 'Martínez', 40, 'laura@gmail.com', 'laura789', TRUE),
	('Pedro', 'Fernández', 45, 'pedro@gmail.com', 'pedro000', FALSE),
	('Ana', 'González', 50, 'ana@gmail.com', 'ana111', TRUE),
	('Juan', 'Pérez', 55, 'juanp@gmail.com', 'juan123', TRUE),
	('Sofía', 'Díaz', 60, 'sofia@gmail.com', 'sofia456', FALSE),
	('Luis', 'Rodríguez', 18, 'luis@gmail.com', 'luis789', TRUE),
	('Elena', 'Sánchez', 20, 'elena@gmail.com', 'elena000', TRUE);