# T-SQL

Transact-SQL (T-SQL) es un lenguaje de programación que nos permite interactuar con bases de datos SQL.

## Comentarios

```sql
-- Comentario de una línea
```

## Variables
    
```sql
DECLARE @variable INT = 1
```

## Tipos de datos

```sql
INT
VARCHAR(50)
BOOLEAN
...
```

|Nombre      |Definición                               |Rango permitido ó Longitud                           |Tamaño  |
|:-----------|:----------------------------------------|:-----------------------------------------|:-------|
|Tinyint     |Entero pequeño que puede o no tener signo|-128 a 127                                |1 byte  |
|Int         |Entero con signo o no                    |-2147483648 a 2147483647                  |4 bytes |
|Smallint    |Entero pequeño con signo o no            |-32768 a 32767                            |2 bytes |
|Mediumint   |Entero de tamaño medio                   |-8388608 a 8388607                        |3 bytes |
|Bigint      |Entero grande                            |-9223372036854775808 a 9223372036854775807|8 bytes |
|Float (M,D)|Longitud de visualización (M) y el número de decimales (D)|(-3.402 823 466 E + 38,1.175 494 351 E-38), 0, (1.175 494 351 E-38,3.402 823 466 351 E + 38)|4bytes|
|Double (M,D)|Define la longitud de visualización (M) y el número de decimales (D). Se ajustará por defecto a 16, 4, donde 4 es el número de decimales.|(1.797 693 134 862 315 7 E + 308,2.225 073 858 507 201 4 E-308), 0, (2.225 073 858 507 201 4 E-308,1.797 693 134 862 315 7 E + 308)|8bytes|
|Decimal (M,D)|Número de coma flotante descomprimido. De Decimal (M, D), si M> D, M + 2 es por lo demás D + 2. |Depende de los valores de M y D|-|
|Char (M)|Almacena la cadena en la memoria, pero no usa todo el espacio. Sirve para guardar textos breves.|De 1 a 255 caracteres|-|
|Varchar (M)|El largo del texto depende de la información que brinda el usuario.|De 1 a 255 caracteres. En la versión de MySQL 5.0.3. cambio a un máximo de 65535 caracteres|-|
|Blob|Guarda la información en lenguaje binario y se utiliza este tipo de datos para almacenar imágenes, sonido y archivos.|Tinyblob, Blob, Midiumblob y Longblob|255 bytes, 65535 bytes, 16777215 bytes y 4GB|
|Text|Empleado para guardar grandes cantidades de texto como blogs, noticias, comentarios, publicaciones, etc.|Tinytext, Text, Mediumtext y Longtext| 255 bytes, 65535 bytes, 16777215 bytes y 4294967295 bytes|
|ENUM|Tipo de datos espacial que se usa para definir valores predeterminados de una lista de valores predefinidos que deben estar separados por comas y entre comillas.|-|Hasta 65535 bytes|
|SET|Lista específica, pero con 64 elementos. Los valores van entrecomillados y se separan por comas.|-|-|
|Date|YYYY-MM-DD|01.01.1000 – 9999-12-31|3 bytes|
|Datetime|Combinación de fecha y hora YYYY-MM-DD HH:MM:SS|1000-01-01 00:00:00 – 9999-12-31 23:59:59|1 byte|
|Timestamp|Parecido al formato de Datetime, solo que es en presente. YYYY-MM-DD HH:MM:SS // YYYY-MM-DD // YY-MM-DD|1970-01-01 hasta 2037-12-31|4 bytes|
|Time|Almacena la hora en HH:MM:SS|-839:59:59 hasta 839:59:59|3 bytes|
|Year|Puede almacenar la información en formato de YY o YYYY|1901/2155|1 byte|

## Operadores

```sql
+ - * / %
```

## Funciones

```sql
SELECT GETDATE()
```

## Ver todas las bases de datos
    
```sql
SHOW DATABASES;
```

## Crear un base de datos

```sql
CREATE DATABASE nombre_base_datos;
```

## Eliminar una base de datos

```sql
DROP DATABASE nombre_base_datos;
```

## Crear una tabla
```sql
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
```

## Insertar datos en una tabla

```sql
INSERT INTO public.usuarios (nombres, apellidos, edad, correo, password, status)
VALUES ('Juan', 'Perez', 30, 'juan@gmail.com', '123456', true);
```

## Ver todos los registros de una tabla

```sql
SELECT * FROM public.usuarios;
```

## WHERE
    
```sql
SELECT nombres, apellidos FROM public.usuarios WHERE id = 1;
```

## Operador LIKE

```sql
SELECT * FROM public.usuarios WHERE nombres LIKE 'J%';
```

## Operadores AND, OR, NOT

```sql
SELECT * FROM public.usuarios WHERE nombres LIKE 'J%' AND edad > 20;
```

##  Operador BETWEEN

```sql
SELECT * FROM public.usuarios WHERE edad BETWEEN 20 AND 30;
```

## Operador ORDER BY

```sql
SELECT * FROM public.usuarios ORDER BY nombres ASC;
SELECT * FROM public.usuarios ORDER BY nombres DESC;
```

## Operador DELETE (Usar con precaución - WHERE es importante)

```sql
DELETE FROM public.usuarios WHERE id = 1;
```

## Operador UPDATE (Usar con precaución - WHERE es importante)

```sql
UPDATE public.usuarios SET nombres = 'Pedro' WHERE id = 2;
```