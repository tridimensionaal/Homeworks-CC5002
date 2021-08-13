#!/usr/bin/python3
# -*- coding: utf-8 -*-
import db
import cgitb
import datetime
cgitb.enable()

avistamiento = db.Avistamiento("localhost", "root", "password")
latest = avistamiento.getLatest()
avis = ""
for data in latest:
    avis += "<tr>"
    for i in range(len(data)-1):
        a = data[i]
        if isinstance(a, datetime.datetime):
            avis += "<td>" + a.strftime('%d/%m/%y %I:%M') + "</td>"
        else:
            avis += "<td>" + a + "</td>"
    a = data[len(data)-1]
    avis += " <td> <img class='responsive-img' src='../media/" + a + "'> </td>"
    avis += "</tr>"

print('Content-type: text/html\r\n\r\n')

with open('static/index.html', 'r') as file:
    s = file.read()
    print(s.format(avis))
