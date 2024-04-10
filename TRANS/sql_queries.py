DDL_QUERY =  '''
-- create database venta;
-- Creación de la tabla categoria
CREATE TABLE categoria (
    idcategoria serial PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255),
    estado BOOLEAN
);

-- Creación de la tabla articulo
CREATE TABLE articulo (
    idarticulo serial PRIMARY KEY,
    idcategoria INTEGER REFERENCES categoria(idcategoria),
    codigo VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio_venta DECIMAL(11,2),
    stock INTEGER,
    descripcion VARCHAR(255),
    imagen VARCHAR(20),
    estado BOOLEAN
);

-- Creación de la tabla persona
CREATE TABLE persona (
    idpersona serial PRIMARY KEY,
    tipo_persona VARCHAR(20) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
);
-- Creación de la tabla rol
CREATE TABLE rol (
    idrol serial PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(255),
    estado BOOLEAN
);
-- Creación de la tabla usuario
CREATE TABLE usuario (
    idusuario serial PRIMARY KEY,
    idrol INTEGER REFERENCES rol(idrol),
    nombre VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50),
    clave BYTEA ,
    estado BOOLEAN
);



-- Creación de la tabla venta
CREATE TABLE venta (
    idventa serial PRIMARY KEY,
    idcliente INTEGER REFERENCES persona(idpersona),
    idusuario INTEGER REFERENCES usuario(idusuario),
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha TIMESTAMP,
    impuesto DECIMAL(4,2),
    total DECIMAL(11,2),
    estado VARCHAR(20)
);

-- Creación de la tabla detalle_venta
CREATE TABLE detalle_venta (
    iddetalle_venta serial PRIMARY KEY,
    idventa INTEGER REFERENCES venta(idventa),
    idarticulo INTEGER REFERENCES articulo(idarticulo),
    cantidad INTEGER,
    precio DECIMAL(11,2),
    descuento DECIMAL(11,2)
);

-- Creación de la tabla ingreso
CREATE TABLE ingreso (
    idingreso serial PRIMARY KEY,
    idproveedor INTEGER REFERENCES persona(idpersona),
    idusuario INTEGER REFERENCES usuario(idusuario),
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha TIMESTAMP,
    impuesto DECIMAL(4,2),
    total DECIMAL(11,2),
    estado VARCHAR(20)
);

-- Creación de la tabla detalle_ingreso
CREATE TABLE detalle_ingreso (
    iddetalle_ingreso serial PRIMARY KEY,
    idingreso INTEGER REFERENCES ingreso(idingreso),
    idarticulo INTEGER REFERENCES articulo(idarticulo),
    cantidad INTEGER,
    precio DECIMAL(11,2)
); '''