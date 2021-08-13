#!/usr/bin/env python3
import db
import cgitb
# import datetime
cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

da = db.DetalleAvistamiento("localhost", "root", "password")

insectos = da.countType("insecto")[0][0]
aracnidos = da.countType("arácnido")[0][0]
miriapodos = da.countType("miriápodo")[0][0]
nose = da.countType("no sé")[0][0]
total = insectos + aracnidos + miriapodos + nose

values = [
        insectos/total,
        aracnidos/total,
        miriapodos/total,
        nose/total
        ]
print(values)
