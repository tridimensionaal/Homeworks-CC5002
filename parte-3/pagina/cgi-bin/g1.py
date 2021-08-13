#!/usr/bin/env python3
import db
import cgitb
import json
cgitb.enable()


print('Content-type: text/html; charset=UTF-8')
print('')


def valuesDate(date):
    global da
    return da.countDate(date[0])[0][0]


def formatDate(date):
    return str(date[0])


da = db.DetalleAvistamiento("localhost", "root", "password")
fechas = da.allDates()
values = list(map(valuesDate, fechas))
fechas = list(map(formatDate, fechas))

dic = {
        "fechas": fechas,
        "values": values
        }
print(json.dumps(dic))
