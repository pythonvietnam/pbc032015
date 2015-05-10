from configloader import class_config
from sys import argv
import MySQLdb

class SqlDB:
    def __init__(self):
    #Ham mo ket noi den database mysql
        try:
            self.dbconfig = class_config('db.cfg')
            self.con = MySQLdb.connect(
                host = self.dbconfig.dict['database'],
                user = self.dbconfig.dict['user'],
                passwd = self.dbconfig.dict['password'],
                db = self.dbconfig.dict['dbname'],)
        
            self.cur = self.con.cursor()
            print "Connect to database successful!!"
        except Exception, e:
            print "Error when connect to database!", e
        
    def __del__(self):
    #Ham dong ket noi
        self.cur.close()
        self.con.close()
    
    def SelectData(self, sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchall()
            return data
        except Exception, e:
            print "Error when execute conmmand SELECT!", e
            
    def InsertData(self, sql, data2insert):
        try:
            self.cur.execute(sql, data2insert)
            self.con.commit()
        except Exception, e:
            self.con.rollback()
            print "Error when execute conmmand INSERT!", e
            
    def UpdateData(self, sql):
        try:
            self.cur.execute(sql)
            self.con.commit()
        except Exception, e:
            self.con.rollback()
            print "Error when execute conmmand UPDATE!", e

    
    
if __name__ == '__main__':
    duc = SqlDB()
#    sql = "INSERT INTO SinhVien (MaSV, TenSV, Diem) VALUES (%s, %s, %s)"
#    data2insert = ('SV02', 'NDMD', 10)
#    duc.InsertData(sql, data2insert)
#    duc.UpdateData('DELETE FROM SinhVien WHERE MaSV = "SV02"')
#    sql = "DELETE FROM SinhVien WHERE MaSV = 'SV1'"
#    duc.UpdateData(sql)
    data = duc.SelectData('select * from SinhVien')
    print data
    
#    string = 'd'
#    for i in range(len(data)):
#        if data[i][2].startswith(string):
#            print '\n', data[i]

    