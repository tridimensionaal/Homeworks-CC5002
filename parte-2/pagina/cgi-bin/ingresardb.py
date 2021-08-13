#!/usr/bin/python3
# -*- coding: utf-8 -*-
import db
import hashlib


def addAvistamiento(comuna, fecha, sector, nombre, email, celular):
    comuna_db = db.Comuna("localhost", "root", "password")
    id_comuna = comuna_db.getId(comuna)[0][0]
    avistamiento = db.Avistamiento("localhost", "root", "password")
    id_avistamiento = avistamiento.add(
            (
                id_comuna, fecha, sector,
                nombre, email, celular
                )
            )
    return id_avistamiento


def addDetalleAvistamiento(fecha, tipo, estado, id_avistamiento):
    detalle_avistamiento = db.DetalleAvistamiento(
            "localhost",
            "root",
            "password"
            )

    id_detalle_avistamiento = detalle_avistamiento.add(
            (
                fecha, tipo,
                estado, id_avistamiento
                )
            )
    return id_detalle_avistamiento


def addFoto(img, id_detalle_avistamiento):
    fileobj = img
    fileb = fileobj.value
    filename = fileobj.filename

    # creación nuevo nombre archvio
    foto = db.Foto("localhost", "root", "password")
    total = foto.countIds()[0][0] + 1
    hash_archivo = str(total) + hashlib.sha256(
            filename.encode()).hexdigest()[0:30]

    # guardar el archivo
    file_path = 'media/' + hash_archivo
    with open(file_path, 'wb') as image:
        image.write(fileb)
    # agregar archivo a la base de datos
    foto.add((hash_archivo, filename, id_detalle_avistamiento))


def addData(
        comuna, sector, nombre, email, celular,
        fecha, tipo, estado, fotos, cantidad_fotos
        ):

    id_avistamiento = addAvistamiento(
            comuna,
            fecha[0],
            sector,
            nombre,
            email,
            celular
            )

    large = len(cantidad_fotos)
    i_fotos = 0
    for i in range(large):
        id_detalle_avistamiento = addDetalleAvistamiento(
                fecha[i], tipo[i], estado[i], id_avistamiento
                )
        num_fotos = int(cantidad_fotos[i])
        for j in range(num_fotos):
            addFoto(fotos[i_fotos], id_detalle_avistamiento)
            i_fotos += 1
