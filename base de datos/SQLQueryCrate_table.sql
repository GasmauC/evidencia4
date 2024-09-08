
CREATE TABLE ProduccionPinceles (
    id INT PRIMARY KEY,
    tipo_pelo_id INT,
    cantidad_cerdas INT NOT NULL,
    encender Bit,
    produccion_total INT,
    costo_material DECIMAL(10, 2),
    FOREIGN KEY (tipo_pelo_id) REFERENCES TiposDePelo(id),
);

CREATE TABLE TiposDePelo (
    id INT  PRIMARY KEY,
    nombre VARCHAR(50)  NOT NULL
);

CREATE TABLE CostosProduccion (
    id INT PRIMARY KEY,
    produccion_id INT,
    costo_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (produccion_id) REFERENCES ProduccionPinceles(id)
);
