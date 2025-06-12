INSERT INTO estudiantes (nombre, edad, ciudad) VALUES 
('Ana Pérez', 19, 'Bogotá'),
('Luis Gómez', 22, 'Medellín'),
('Carlos Díaz', 20, 'Cali'),
('María López', 23, 'Bogotá'),
('Jorge Ramírez', 18, 'Barranquilla');

SELECT * FROM estudiantes;

SELECT * FROM estudiantes
WHERE ciudad = 'Bogotá';

SELECT * FROM estudiantes
WHERE edad > 20;