#!/usr/bin/env python3
import db
import cgitb
import json
# import datetime
cgitb.enable()


print('Content-type: text/html; charset=UTF-8')
print('')


def nameComuna(id_comuna):
    global comuna
    return comuna.getNameFromId(id_comuna[0])[0][0]


def fotosComuna(id_comuna):
    global comuna
    return comuna.fotosFromIdComuna(id_comuna[0])


def fotosFormat(foto):
    form = []
    for i in range(len(foto)):
        if i==1:
            form += [str(foto[i])]
        else:
            form += [foto[i]]
    return form

avis = db.Avistamiento("localhost", "root", "password")
comuna = db.Comuna("localhost", "root", "password")

id_comunas = avis.getComunas()

name_comunas = list(map(nameComuna, id_comunas))
fotos_comunas = list(map(fotosComuna, id_comunas))

for i in range(len(fotos_comunas)):
    fotos_comunas[i] = list(map(fotosFormat, fotos_comunas[i]))



dic = {
        "nombres": name_comunas,
        "fotos": dict(zip(name_comunas, fotos_comunas))
        }
print(json.dumps(dic))
