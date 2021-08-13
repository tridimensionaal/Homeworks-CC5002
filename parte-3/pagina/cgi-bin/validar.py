#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db
import re
import os
import filetype

error = []


def errorString(tipo, string):
    global error
    error += [tipo + " inválido: " + string + "."]


def errorFoto(string, msg):
    global error
    error += ["Foto inválida : " + string + ", " + msg]


def validateRegex(regex, string, tipo):
    data_regex = re.match(regex, string)
    if (data_regex is None):
        errorString(tipo, string)


def validateInList(lista, string, tipo):
    if (string not in lista):
        errorString(tipo, string)


# Función para validar la comuna
def validateCom(data):
    comuna = db.Comuna("localhost", "root", "password")
    if len(comuna.getName(data)) == 0:
        errorString("Comuna", data)


# Función para validar la region
def validateReg(data):
    region = db.Region("localhost", "root", "password")
    if len(region.getName(data)) == 0:
        errorString("Región", data)


def validateSector(data):
    if data == "":
        return
    else:
        regex = "^[A-zÁ-ú]+( ([A-zÁ-ú]|[0-9])+)*$"
        validateRegex(regex, data, "Sector")


def validateNombre(data):
    regex = """^[A-zÁ-ú]+$|^[A-zÁ-ú]+ [A-zÁ-ú]+$|
     ^[A-zÁ-ú]+ [A-zÁ-ú]+ [A-zÁ-ú]+$|
     ^[A-zÁ-ú]+ [A-zÁ-ú]+ [A-zÁ-ú]+ [A-zÁ-ú]+$
    """
    validateRegex(regex, data, "Nombre")


def validateEmail(data):
    regex = "^[A-z0-9]+([._]|[A-z0-9]*)*[@][a-z]+([.][a-z]+)+$"
    validateRegex(regex, data, "Email")


def validateNumero(data):
    regex = "^[+]?[(]?[0-9]{3}[)]?[ .]?[0-9]{3}[- .]?[0-9]{3,6}$"
    validateRegex(regex, data, "Número")


def validateFecha(data):
    regex = "^[0-9]{4}[-][0-9]{2}[-][0-9]{2}[\r][\n][0-9]{2}[:][0-9]{2}$"
    validateRegex(regex, data, "Fecha")


def validateTipo(data):
    lista = ["Insecto", "Arácnido", "Miriápodo", "No sé"]
    validateInList(lista, data, "Tipo")


def validateEstado(data):
    lista = ["Vivo", "Muerto", "No sé"]
    validateInList(lista, data, "Estado")


def validateFoto(data):
    # 10 MB
    MAX_FILE_SIZE = 10000 * 1000

    fileobj = data
    filename = fileobj.filename

    if not filename:
        errorFoto("", "no se subió ningún archivo.")
        return

    try:
        size = os.fstat(fileobj.file.fileno()).st_size
    except:
        errorFoto(filename, "el archivo no es una imagen.")
        return

    if size > MAX_FILE_SIZE:
        errorFoto(filename, "el tamaño máximo del archivo es 10MB.")
        return

    # verificamos el tipo, si no es valido lo borramos de la db
    tipo = filetype.guess(fileobj.file.read())
    if (
            tipo.mime != 'image/png' and tipo.mime != 'image/jpg' and
            tipo.mime != 'image/jpeg'
            ):
        errorFoto(filename, "el archivo no es una imagen.")
    return


def validate(data):
    global error
    validateReg(data[0])
    validateCom(data[1])
    validateSector(data[2])
    validateNombre(data[3])
    validateEmail(data[4])
    validateNumero(data[5])
    for e in data[6]:
        validateFecha(e)
    for e in data[7]:
        validateTipo(e)
    for e in data[8]:
        validateEstado(e)
    for e in data[9]:
        validateFoto(e)

    return error
