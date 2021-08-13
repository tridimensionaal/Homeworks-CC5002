#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgitb
import cgi
import validar as v
import ingresardb as idb
cgitb.enable()


def getValue(x):
    return x.value


def getValues(li):
    li = map(getValue, li)
    return list(li)


def transformForm(form):
    if isinstance(form, list):
        return getValues(form)
    else:
        return [form.value]


print("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()
region = form['region'].value
comuna = form['comuna'].value
sector = form['sector'].value
nombre = form['nombre'].value
email = form['email'].value
celular = form['celular'].value
fecha = transformForm(form['dia-hora-avistamiento'])
tipo = transformForm(form['tipo-avistamiento'])
estado = transformForm(form['estado-avistamiento'])
cantidad_fotos = transformForm(form['fotos'])
foto = form['foto-avistamiento']
if (not isinstance(foto, list)):
    foto = [foto]

data = (region,
        comuna,
        sector,
        nombre,
        email,
        celular,
        fecha,
        tipo,
        estado,
        foto)
error = v.validate(data)

if len(error) == 0:
    msg = "<h3> ¡Tu avistamiento ha sido informado con éxito! </h3>"
    idb.addData(
            comuna, sector, nombre, email, celular,
            fecha, tipo, estado, foto, cantidad_fotos
            )
    with open('static/avistamiento.html', 'r') as file:
        s = file.read()
        print(s.format("", msg))

else:
    msg = "<h3> Ha ocurrido un error con la información entregada </h3>"

    msg += "<ul>"

    for e in error:
        msg += "<li>" + e + "</li>"
    msg += "</ul>"

    with open('static/avistamiento.html', 'r') as file:
        volver = """<li><a href='javascript:history.back()'>
        Volver al formulario</a></li>"""
        s = file.read()
        print(s.format(volver, msg))
