-- CONCAT (Concatena diferente caracteres)
SELECT id, CONCAT(nombres, ' ', apellidos) AS nombres_completos FROM public.usuarios;

-- LENGTH (Calcula la longitud de caracteres)
SELECT nombres FROM public.usuarios WHERE LENGTH(nombres) > 4;

-- UPPER, LOWER (Convierten a mayusculas y minusculas respectivamente)
SELECT id, UPPER(nombres) as nombres, LOWER(apellidos) as apellidos FROM public.usuarios;

-- TRIM (Quita los espacios en blanco)
SELECT TRIM(' Soy un texto con espacios ');

-- LEFT y RIGHT (Toma la cantidad de valores que querramos del lado que querramos)
SELECT * FROM public.usuarios WHERE RIGHT(nombres, 2) = 'an';
SELECT RIGHT('Hola mundo!', 8);
SELECT LEFT('Hola mundo!', 8);

-- TRUNCATE (limita la cantidad de decimasles)
SELECT TRUNC(0.123856, 3);

-- RANDOM (Generar numeros aleatorios entre 0 y 1)
SELECT FLOOR(RANDOM() * 10) + 1 AS aleatorio;

-- NOW (Tomar el tiempo actual)
SELECT NOW();
SELECT EXTRACT(SECOND FROM NOW());
SELECT EXTRACT(MINUTE FROM NOW());
SELECT EXTRACT(HOUR FROM NOW());
SELECT EXTRACT(DAY FROM NOW());
SELECT NOW() + INTERVAL '20 days';
SELECT (NOW() + INTERVAL '20 days')::date;