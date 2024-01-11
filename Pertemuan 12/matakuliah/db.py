# db.py

import mysql.connector as mc

class DBConnection:

    def __init__(self):
        self.host = "sql.freedb.tech"
        self.port = 3306
        self.name = "freedb_rsatsat"
        self.user = "freedb_rsatsat"
        self.password = "Hg$*v@h6r9N4e24"
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()

    @property
    def connection_status(self):
        return self.connected

    def connect(self):
        try:
            self.conn = mc.connect(host=self.host,
                                   port=self.port,
                                   database=self.name,
                                   user=self.user,
                                   password=self.password)

            self.connected = True
            self.cursor = self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def print_connection_info(self):
        print(f"Connected to the database at {self.host}:{self.port}, database: {self.name}")

    def disconnect(self):
        if self.connected:
            self.conn.close()
        else:
            self.conn = None

    def findOne(self, sql, values=None):
        self.connect()
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    def findAll(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql, val):
        self.connect()
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def update(self, sql, val):
        self.connect()
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def delete(self, sql, values=None):
        self.connect()
        if values:
            self.cursor.execute(sql, values)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def getById(self, sql, id):
        self.connect()
        self.cursor.execute(sql, (id,))
        self.result = self.cursor.fetchone()
        return self.result

    def show(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    @property
    def info(self):
        if self.connected:
            return "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."
