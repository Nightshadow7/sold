CREATE SCHEMA `facturas` ;
USE `facturas`;
CREATE TABLE cliente (
    ID_Cliente INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Telefono VARCHAR(15),
    Ciudad VARCHAR(100),
    Fecha_Registro DATE NOT NULL
);
CREATE TABLE proyecto (
  ID_Proyecto INT PRIMARY KEY AUTO_INCREMENT,
  Nombre_Proyecto VARCHAR(255) NOT NULL,
  Cliente_ID INT,
  Fecha_Inicio DATE,
  Fecha_Terminacion DATE,
  Estado VARCHAR(50),
  Presupuesto DECIMAL(10, 2),
  FOREIGN KEY (Cliente_ID) REFERENCES cliente(ID_Cliente) ON DELETE SET NULL
);
CREATE TABLE venta (
  ID_Venta INT PRIMARY KEY AUTO_INCREMENT,
  ID_Cliente INT,
  ID_Proyecto INT,
  Fecha_Venta DATE NOT NULL,
  Monto DECIMAL(10, 2),
  Metodo_de_Pago VARCHAR(50),
  FOREIGN KEY (ID_Cliente) REFERENCES cliente(ID_Cliente) ON DELETE CASCADE,
  FOREIGN KEY (ID_Proyecto) REFERENCES proyecto(ID_Proyecto) ON DELETE CASCADE
);

-- Script para insertar datos 
-- Insertar registros en la tabla cliente
INSERT INTO cliente (Nombre, Email, Telefono, Ciudad, Fecha_Registro) VALUES
('Juan Pérez', 'juan.perez@example.com', '555-1234', 'Ciudad A', '2023-01-15'),
('Maria López', 'maria.lopez@example.com', '555-5678', 'Ciudad B', '2023-02-20'),
('Carlos Ruiz', 'carlos.ruiz@example.com', '555-9876', 'Ciudad C', '2023-03-10'),
('Ana García', 'ana.garcia@example.com', '555-3456', 'Ciudad D', '2023-04-12'),
('Pedro Torres', 'pedro.torres@example.com', '555-8765', 'Ciudad A', '2023-05-22'),
('Laura Sánchez', 'laura.sanchez@example.com', '555-6543', 'Ciudad B', '2023-06-30'),
('Luis Gómez', 'luis.gomez@example.com', '555-3212', 'Ciudad C', '2023-07-05'),
('Isabel Fernández', 'isabel.fernandez@example.com', '555-2345', 'Ciudad D', '2023-08-08'),
('Ricardo Mendoza', 'ricardo.mendoza@example.com', '555-6789', 'Ciudad A', '2023-09-14'),
('Sofia Castro', 'sofia.castro@example.com', '555-4321', 'Ciudad B', '2023-10-01');

-- Insertar registros en la tabla proyecto (asociando con IDs de cliente válidos)
INSERT INTO proyecto (Nombre_Proyecto, Cliente_ID, Fecha_Inicio, Fecha_Terminacion, Estado, Presupuesto) VALUES
('Proyecto Alpha', 1, '2023-02-01', '2023-07-01', 'Completado', 5000.00),
('Proyecto Beta', 2, '2023-03-15', '2023-09-15', 'En Proceso', 8000.00),
('Proyecto Gamma', 3, '2023-04-20', '2023-10-20', 'En Proceso', 12000.00),
('Proyecto Delta', 4, '2023-05-01', NULL, 'Pendiente', 4000.00),
('Proyecto Epsilon', 5, '2023-06-10', '2023-11-10', 'Completado', 15000.00),
('Proyecto Zeta', 6, '2023-07-15', NULL, 'En Proceso', 7000.00),
('Proyecto Eta', 7, '2023-08-01', NULL, 'Pendiente', 6000.00),
('Proyecto Theta', 8, '2023-09-05', NULL, 'En Proceso', 20000.00),
('Proyecto Iota', 9, '2023-10-01', NULL, 'En Proceso', 3000.00),
('Proyecto Kappa', 10, '2023-10-15', NULL, 'Pendiente', 11000.00);

-- Insertar registros en la tabla venta (asociando con IDs de cliente y proyecto válidos)
INSERT INTO venta (ID_Cliente, ID_Proyecto, Fecha_Venta, Monto, Metodo_de_Pago) VALUES
(1, 1, '2023-02-05', 5000.00, 'Transferencia'),
(2, 2, '2023-03-18', 8000.00, 'Tarjeta de Crédito'),
(3, 3, '2023-04-22', 12000.00, 'Efectivo'),
(4, 4, '2023-05-05', 4000.00, 'Transferencia'),
(5, 5, '2023-06-15', 15000.00, 'Tarjeta de Crédito'),
(6, 6, '2023-07-20', 7000.00, 'Efectivo'),
(7, 7, '2023-08-03', 6000.00, 'Transferencia'),
(8, 8, '2023-09-07', 20000.00, 'Efectivo'),
(9, 9, '2023-10-03', 3000.00, 'Tarjeta de Crédito'),
(10, 10, '2023-10-18', 11000.00, 'Transferencia');


-- Mostrar datos de la tabla cliente
SELECT * FROM cliente;

-- Mostrar datos de la tabla proyecto
SELECT * FROM proyecto;

-- Mostrar datos de la tabla venta
SELECT * FROM venta;