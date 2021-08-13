SELECT AV.id, CO.nombre, AV.dia_hora, AV.sector, AV.nombre, AV.email 
FROM avistamiento AV, comuna CO, foto
WHERE AV.comuna_id = CO.id;
