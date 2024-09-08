
--Insertando datos en la tabla TiposDePelo

INSERT INTO TiposDePelo(id,nombre)
VALUES
    (1,'Cerda'),
    (2,'sintetico'),
    (3,'Nylon'),
	(4,'Mixto'),
	(5,'Cerda de tejón');


-- Insertando datos en la tabla ProduccionPinceles
INSERT INTO ProduccionPinceles (id,tipo_pelo_id, cantidad_cerdas, encender, produccion_total, costo_material)
VALUES
    (1,1, 500, 1, 1000, 500.00),
    (2,2, 300, 0, 800, 350.00),
    (3,3, 200, 1, 500, 800.00),
	(4,4, 100, 1, 1000,400.00),
	(5,5, 200, 0, 50,  900.00);
    
	-- Insertando datos en la tabla CostosProduccion
INSERT INTO CostosProduccion (id,produccion_id, costo_total)
VALUES
    (1,1, 1000.00),
    (2,2, 850.00),
    (3,3, 1200.00),
	(4,4, 2000.00),
	(5,5, 6000.00);
    
   

    --CONSULTAS:
    --TABLA PRODUCIONPINCELES:

    --Calcular el promedio de cerdas por tipo de pincel:
	SELECT t.nombre, AVG(p.cantidad_cerdas) AS promedio_cerdas
	FROM ProduccionPinceles p
	INNER JOIN TiposDePelo t ON p.tipo_pelo_id = t.id
	GROUP BY t.nombre;
	
	--Obtener los detalles de los pinceles de tipo sintético y su costo total

	SELECT p.id, p.cantidad_cerdas, c.costo_total
	FROM ProduccionPinceles p
	INNER JOIN CostosProduccion c ON p.id = c.produccion_id
	INNER JOIN TiposDePelo t ON p.tipo_pelo_id = t.id
	WHERE t.nombre = 'sintetico';
	
	--TIPOSDEPELO:

	SELECT * FROM TiposDePelo WHERE nombre = 'Cerda de tejón';

	--TABLA COSTOPRODUCCION:

	--Obtener el costo total de producción de todos los pinceles:
	SELECT SUM(costo_total) AS costo_total_general FROM CostosProduccion;
	
	--Encontrar el pincel con el costo de producion mas alto:
	SELECT * FROM CostosProduccion
	ORDER BY costo_total DESC;
	



