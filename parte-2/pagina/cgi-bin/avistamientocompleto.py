#!/usr/bin/python3
# -*- coding: utf-8 -*-
import db
import cgitb
import cgi
cgitb.enable()

form = cgi.FieldStorage()
avis_id = form['id'].value


def avistamiento():
    db_avistamientos = db.Avistamiento("localhost", "root", "password")

    avistamientos = db_avistamientos.get(avis_id)

    return avistamientos


def detalle_avistamientos():
    db_detalle_avistamientos = db.DetalleAvistamiento(
            "localhost",
            "root",
            "password"
            )
    detalle_avistamient_d = db_detalle_avistamientos.allAvis(avis_id)
    foto = db.Foto(
            "localhost",
            "root",
            "password"
            )

    msg = ""
    base = """<h4> Información de avistamiento </h4>
           <div class='dato'>
             <div class='leyenda'>Día-hora</div>
             {0}
           </div>
           <div class='dato'>
             <div class='leyenda'>Tipo</div>
             {1}
          </div>
          <div class='dato'>
            <div class='leyenda'>Estado</div>
            {2}
          </div>
          <div class='dato'>
            <div class='leyenda'>Fotos</div>
          </div>
          """
    for avis in detalle_avistamient_d:
        base_c = base.format(
                avis[1].strftime('%d/%m/%y %I:%M'),
                avis[2],
                avis[3]
            )
        all_photos = foto.allPhotosId(avis[0])

        for photo in all_photos:
            base_c += """<a href='imagen.py?ruta={0}&avis={1}'>
            <img class='avis-img' src='../media/{0}' alt=''>
            </a>
            """.format(photo[0], avis_id)

        msg += base_c

    return msg


avistamiento_d = avistamiento()[0]
region = avistamiento_d[0]
comuna = avistamiento_d[1]
sector = avistamiento_d[2]
nombre = avistamiento_d[3]
email = avistamiento_d[4]
celular = avistamiento_d[5]
print('Content-type: text/html\r\n\r\n')
with open('static/avistamiento-completo.html', 'r') as file:
    s = file.read()
    print(s.format(
        region,
        comuna,
        sector,
        nombre,
        email,
        celular,
        detalle_avistamientos()
        ))
