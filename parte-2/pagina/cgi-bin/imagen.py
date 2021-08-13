#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgitb
import cgi
cgitb.enable()

form = cgi.FieldStorage()
ruta = form['ruta'].value
avis_id = form['avis'].value

with open('static/imagen.html', 'r') as file:
    s = file.read()
    print(s.format(
        avis_id,
        ruta
        ))
