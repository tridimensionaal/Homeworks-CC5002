#!/usr/bin/python3
# -*- coding: utf-8 -*-
import db
import cgitb
import datetime
cgitb.enable()


def avistamientos():
    msg = ""
    db_avistamientos = db.Avistamiento("localhost", "root", "password")

    detalle_avistamiento = db.DetalleAvistamiento(
            "localhost", "root", "password"
            )

    avistamientos = db_avistamientos.getAll()

    foto = db.Foto("localhost", "root", "password")

    for avis in avistamientos:
        msg += "<tr>"
        for d in avis:
            if isinstance(d, int):
                id_int = str(d)
                msg += "<td> <a href='../cgi-bin/avistamientocompleto.py?id=" + id_int + "'>" + id_int + "</a></td>"
            elif isinstance(d, datetime.datetime):
                msg += "<td>" + d.strftime('%d/%m/%y %I:%M') + "</td>"
            else:
                msg += "<td>" + d + "</td>"

        total_avis = detalle_avistamiento.totalAvis(avis[0])
        msg += "<td>" + str(len(total_avis)) + "</td>"

        total_fotos = 0
        for da in total_avis:
            total_fotos += foto.countAvis(da[0])[0][0]
        msg += "<td>" + str(total_fotos) + "</td>"

    return msg


print('Content-type: text/html\r\n\r\n')

with open('static/avistamientos.html', 'r') as file:
    s = file.read()
    print(s.format(avistamientos()))
