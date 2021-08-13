SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

SELECT dia_hora, nombre, sector, tipo, ruta_archivo FROM (
    SELECT tabla1.id, dia_hora, nombre, sector, tipo, ruta_archivo FROM (
        SELECT DA.id, DA.dia_hora, CO.nombre, AV.sector, DA.tipo
        FROM avistamiento AV, detalle_avistamiento DA, comuna CO
        WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id 
        ORDER BY DA.dia_hora DESC LIMIT 5
    ) tabla1
    LEFT JOIN foto F
    ON tabla1.id = F.detalle_avistamiento_id 
    GROUP by tabla1.id
) table2;



