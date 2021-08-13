#!/usr/bin/env python3
import db
import cgitb
import json
# import datetime
cgitb.enable()


print('Content-type: text/html; charset=UTF-8')
print('')


def valuesVivo(month):
    global da
    return da.countState(month, "vivo")[0][0]


def valuesMuerto(month):
    global da
    return da.countState(month, "muerto")[0][0]


def valuesNose(month):
    global da
    return da.countState(month, "no sé")[0][0]


da = db.DetalleAvistamiento("localhost", "root", "password")
months = [i for i in range(1, 13)]
vivos = list(map(valuesVivo, months))
muertos = list(map(valuesMuerto, months))
nose = list(map(valuesNose, months))

dic = {
        "vivos": vivos,
        "muertos": muertos,
        "no sé": nose
        }

print(json.dumps(dic))
