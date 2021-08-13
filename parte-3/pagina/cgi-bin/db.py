import mysql.connector


class Table:
    def __init__(self, host, user, password):
        self.db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database="tarea2",
                auth_plugin='mysql_native_password'
                )
        self.cursor = self.db.cursor()


class Comuna(Table):
    def getName(self, name):
        sql = "SELECT nombre FROM comuna WHERE nombre=%s"
        self.cursor.execute(sql, (name, ))
        return self.cursor.fetchall()

    def getId(self, name):
        sql = "SELECT id FROM comuna WHERE nombre=%s"
        self.cursor.execute(sql, (name, ))
        return self.cursor.fetchall()

    def getNameFromId(self, c_id):
        sql = "SELECT nombre FROM comuna WHERE id=%s"
        self.cursor.execute(sql, (c_id, ))
        return self.cursor.fetchall()

    def fotosFromIdComuna(self, id_comuna):
        sql = """SELECT AV.id, DA.dia_hora,
        DA.tipo, DA.estado, F.ruta_archivo
        FROM avistamiento AV, detalle_avistamiento DA, foto F
        WHERE AV.comuna_id={}
        AND AV.id=DA.avistamiento_id
        AND F.detalle_avistamiento_id=DA.id""".format(id_comuna)

        self.cursor.execute(sql)
        return self.cursor.fetchall()


class Region(Table):
    def getName(self, name):
        sql = "SELECT nombre FROM region WHERE nombre=%s"
        self.cursor.execute(sql, (name, ))
        return self.cursor.fetchall()


class Avistamiento(Table):
    def getLatest(self):
        sql = """SET GLOBAL
        sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))"""

        sql2 = """SELECT dia_hora, nombre, sector, tipo, ruta_archivo
        FROM ( SELECT tabla1.id, dia_hora, nombre, sector, tipo, ruta_archivo
        FROM (SELECT DA.id, DA.dia_hora, CO.nombre, AV.sector, DA.tipo
        FROM avistamiento AV, detalle_avistamiento DA, comuna CO
        WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id
        ORDER BY DA.dia_hora DESC LIMIT 5
        ) tabla1
        LEFT JOIN foto F
        ON tabla1.id = F.detalle_avistamiento_id
        GROUP by tabla1.id
        ) table2;
        """
        self.cursor.execute(sql)
        self.cursor.execute(sql2)
        return self.cursor.fetchall()

    def getComunas(self):
        sql = """SELECT DISTINCT comuna_id
        FROM avistamiento"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def add(self, data):
        sql = """INSERT INTO avistamiento
        (comuna_id, dia_hora, sector, nombre, email, celular)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (*data, ))
        self.db.commit()
        return self.cursor.lastrowid

    def getAll(self):
        sql = """SELECT AV.id, AV.dia_hora, CO.nombre, AV.sector, AV.nombre
        FROM avistamiento AV, comuna CO
        WHERE AV.comuna_id = CO.id
        ORDER BY AV.id DESC
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get(self, avis_id):
        sql = """SELECT RE.nombre, CO.nombre, AV.sector,
        AV.nombre, AV.email, AV.celular
        FROM avistamiento AV, comuna CO, region RE
        WHERE AV.comuna_id = CO.id
        AND RE.id = CO.region_id
        AND AV.id = {}""".format(avis_id)

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def idsFromComuna(self, id_comuna):
        sql = """SELECT COUNT(*)
        FROM avistamiento AV, detalle_avistamiento DA, foto F
        WHERE AV.comuna_id={}
        AND AV.id=DA.avistamiento_id
        AND F.detalle_avistamiento_id=DA.id""".format(id_comuna)

        self.cursor.execute(sql)
        return self.cursor.fetchall()


class DetalleAvistamiento(Table):
    def add(self, data):
        sql = """INSERT INTO detalle_avistamiento
        (dia_hora, tipo, estado, avistamiento_id)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(sql, (*data, ))
        self.db.commit()
        return self.cursor.lastrowid

    def totalAvis(self, avis_id):
        sql = """SELECT id
        FROM detalle_avistamiento
        WHERE avistamiento_id={}""".format(avis_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def allAvis(self, avis_id):
        sql = """SELECT id, dia_hora, tipo, estado
        FROM detalle_avistamiento
        WHERE avistamiento_id={}""".format(avis_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def countType(self, tipo):
        sql = """SELECT count(*)
        FROM detalle_avistamiento
        WHERE tipo='{}'""".format(tipo)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def countState(self, month, state):
        sql = """select count(*)
        from detalle_avistamiento
        where extract(MONTH from dia_hora)={0}
        and estado='{1}'""".format(month, state)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def allDates(self):
        sql = """SELECT DISTINCT distinct DATE(dia_hora)
        FROM detalle_avistamiento
        ORDER BY dia_hora ASC"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def countDate(self, date):
        sql = """SELECT COUNT(*)
        FROM detalle_avistamiento
        WHERE DATE(dia_hora)='{}'""".format(date)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


class Foto(Table):
    def countIds(self):
        sql = "SELECT COUNT(id) from foto"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def add(self, data):
        sql = """INSERT INTO foto
        (ruta_archivo, nombre_archivo, detalle_avistamiento_id)
        VALUES (%s, %s, %s);
        """
        self.cursor.execute(sql, (*data, ))
        self.db.commit()

    def countAvis(self, avis_id):
        sql = """SELECT COUNT(id)
        FROM foto
        WHERE detalle_avistamiento_id={}""".format(avis_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def allPhotosId(self, avis_id):
        sql = """SELECT ruta_archivo
        FROM foto
        WHERE detalle_avistamiento_id={}""".format(avis_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
