from configloader import class_config
from sys import argv
import MySQLdb

dbconfig = class_config('db.cfg')
print dbconfig.dict['database']

try:
    con = MySQLdb.connect(
        host = dbconfig.dict['database'],
        user = dbconfig.dict['user'],
        passwd = dbconfig.dict['password'],
        db = dbconfig.dict['dbname'],)
        
    cur = con.cursor()
    print "Connect to database successful!!"
    
    cur.execute("select * from CUSTOMERS")

#Select du lieu
    row1 = cur.fetchone()
    print "Noi dung row1: ", row1
    
    row2 = cur.fetchone()
    print "Noi dung row1: ", row2[2]
    
    rows = cur.fetchall()
    print "Noi dung rows: ", rows

#Insert du lieu
    sql2 = "INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) VALUES (%s, %s, %s, %s, %s)"
    data2insert = (10, 'DucNC', 23, 'HCM', 6500.00)
    try:
        cur.execute(sql2, data2insert)
        con.commit()
    except Exception, e:
        con.rollback()
        print "Co loi insert", e
    
#Update 
    sql3 = "update CUSTOMERS set NAME = 'NDMD' WHERE ID = 1"
    try:
        cur.execute(sql3)
        con.commit()
    except Exception, e:
        con.rollback()
        print e

except Exception, e:
    print e

finally:
    cur.close()
    con.close()
    
'''
class DB:
    def __init__(self):
        self.line1 = ''
        self.connect()
        self.fetch()
        self.close()
        
    def connect(self,dbhost,dbuser,dbpasswd,dbname):
        self.con = MySQLdb.connect(host='103.17.237.28',user='ducnc',passwd='123123',db='test')
        self.cur = self.con.cursor()
    
    def fetch(self):
        self.line1 = self.cur.fetchone()
        print self.line1
        
    def close(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    a = DB
    print a


    if len(argv) != 2:
        print 'Hay nhap theo dinh dang "python main.py path_to_configfile"'
        exit()
    script, file = argv
    duc = class_config(file)
    x = duc.dict
#    print duc.__doc__
    print_info(x)

    
    for key in duc.dict:
        if key == 'database':
            print "Database name is: ", duc.dict[key]
        elif key == 'user':
            print "User name is: ", duc.dict[key]
        elif key == 'password':
            print "Password is: ", duc.dict[key]
'''