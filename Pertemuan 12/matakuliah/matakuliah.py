from db import DBConnection as mydb

class Matakuliah:

    def __init__(self):
        self.__id_matakuliah = None
        self.__kodemk = None
        self.__namamk = None
        self.__sks = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id_matakuliah

    @id.setter
    def id(self, value):
        self.__id_matakuliah = value

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def namamk(self):
        return self.__namamk

    @namamk.setter
    def namamk(self, value):
        self.__namamk = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodemk, self.__namamk, self.__sks)
        sql = "INSERT INTO matakuliah (kodemk, namamk, sks) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self):  
        self.conn = mydb()
        val = (self.__namamk, self.__sks, self.__id_matakuliah)
        sql = "UPDATE matakuliah SET namamk = %s, sks = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self):  
        self.conn = mydb()
        sql = "DELETE FROM matakuliah WHERE id = %s"
        self.affected = self.conn.delete(sql, (self.__id_matakuliah,))
        self.conn.disconnect()
        return self.affected

    def getById(self):  
        self.conn = mydb()
        sql = "SELECT * FROM matakuliah WHERE id = %s"
        self.result = self.conn.findOne(sql, (self.__id_matakuliah,))
        if self.result is not None:
            self.__kodemk = self.result[1]
            self.__namamk = self.result[2]
            self.__sks = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodemk = ''
            self.__namamk = ''
            self.__sks = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        self.conn.disconnect()
        return self.result
