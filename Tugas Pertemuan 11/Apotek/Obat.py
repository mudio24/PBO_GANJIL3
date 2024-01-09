from db import DBConnection as mydb

class Obat:

    def __init__(self):
        self.__id = None
        self.__kode_obat = None
        self.__nama_obat = None
        self.__berat = None
        self.__bentuk = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id

    @property
    def kode_obat(self):
        return self.__kode_obat

    @kode_obat.setter
    def kode_obat(self, value):
        self.__kode_obat = value

    @property
    def nama_obat(self):
        return self.__nama_obat

    @nama_obat.setter
    def nama_obat(self, value):
        self.__nama_obat = value

    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, value):
        self.__berat = value

    @property
    def bentuk(self):
        return self.__bentuk

    @bentuk.setter
    def bentuk(self, value):
        self.__bentuk = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_obat, self.__nama_obat, self.__berat, self.__bentuk)
        sql = "INSERT INTO obat (kode_obat, nama_obat, berat, bentuk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_obat, self.__nama_obat, self.__berat, self.__bentuk, id)
        sql = "UPDATE obat SET kode_obat = %s, nama_obat = %s, berat=%s, bentuk=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM obat WHERE id=%s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect
        return self.affected

    
    def cari(self, teks_pencarian):
        self.conn = mydb()
        sql = f"SELECT kode_obat, nama_obat, berat, bentuk FROM obat WHERE kode_obat LIKE '%{teks_pencarian}%' OR nama_obat LIKE '%{teks_pencarian}%'"
        self.result = self.conn.findAll(sql)
        return self.result


    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM obat WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_obat = self.result[1]
        self.__nama_obat = self.result[2]
        self.__berat = self.result[3]
        self.__bentuk = self.result[4]
        self.conn.disconnect
        return self.result

    def getByKodeObat(self, kode_obat):
        self.conn = mydb()
        sql = "SELECT * FROM obat WHERE kode_obat='" + str(kode_obat) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result != None):
            self.__kode_obat = self.result[1]
            self.__nama_obat = self.result[2]
            self.__berat = self.result[3]
            self.__bentuk = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_obat = ''
            self.__nama_obat = ''
            self.__berat = ''
            self.__bentuk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM obat"
        self.result = self.conn.findAll(sql)
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT kode_obat, nama_obat, berat, bentuk FROM obat"  # Hanya ambil kolom yang diperlukan
        self.result = self.conn.findAll(sql)
        return self.result


# Contoh penggunaan:
C = Obat()
D = C.getAllData()
print(D)
