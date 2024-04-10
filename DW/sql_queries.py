DDL_QUERY =  '''
CREATE TABLE dim_articulo (
    articulo_id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50),
    nombre VARCHAR(100),
    precio_venta DECIMAL(11, 2),
    stock INT,
    descripcion VARCHAR(255),
    imagen VARCHAR(20)
);

-- Dimension Cliente
CREATE TABLE dim_cliente (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_persona VARCHAR(20),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
);

-- Dimension Usuario
CREATE TABLE dim_usuario (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50),
    rol_id INT
    -- Aquí puedes agregar una clave foránea a dim_rol si tienes una tabla de roles
    -- FOREIGN KEY (rol_id) REFERENCES dim_rol(rol_id)
);

-- Dimension Categoria
CREATE TABLE dim_categoria (
    categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    descripcion VARCHAR(255)
);

-- Dimension Tiempo (Este es un ejemplo, necesitarás insertar los datos manualmente o generarlos con un script)
CREATE TABLE dim_tiempo (
    fecha DATE PRIMARY KEY,
    dia INT,
    mes INT,
    año INT,
    trimestre INT,
    dia_semana VARCHAR(9)
);

-- Dimension Rol (si aplicable)
CREATE TABLE dim_rol (
    rol_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(255)
);

-- Tabla de hechos FactVentas
CREATE TABLE fact_ventas (
    fact_venta_id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    cantidad INT,
    precio_unitario DECIMAL(11, 2),
    descuento DECIMAL(11, 2),
    impuesto DECIMAL(4, 2),
    total DECIMAL(11, 2),
    articulo_id INT,
    cliente_id INT,
    usuario_id INT,
    categoria_id INT,
    -- Aquí puedes agregar claves foráneas a las dimensiones correspondientes
    FOREIGN KEY (articulo_id) REFERENCES dim_articulo(articulo_id),
    FOREIGN KEY (cliente_id) REFERENCES dim_cliente(cliente_id),
    FOREIGN KEY (usuario_id) REFERENCES dim_usuario(usuario_id),
    FOREIGN KEY (categoria_id) REFERENCES dim_categoria(categoria_id)
);
 '''