#!/usr/bin/python

# Chuong trinh tinh toan nhan / chia / cong / tru hai so
from sys import argv

def hello():
    print "Hello world"
    
def cong(a, b):
    return float(a) + float(b)
    
def tru(a, b):
    return float(a) - float(b)

def nhan(a, b):
    return float(a) * float(b)

def chia(a, b):
    return float(a) / float(b)

if __name__ == '__main__':

    print "Chuong trinh tinh toan cong tru nhan chia 2 so tu nhien"

    try:
        tenfile, a, pheptoan, b = argv
    except:
        print "Nhap cac tham so theo dang 'python pheptoan a b'"
        exit()

    if pheptoan == '+':
        print "Tong la:", cong(a, b)
        
    elif pheptoan == '-':
        print "Hieu la", tru(a, b)
    elif pheptoan == '*':
        print "Tich la ", nhan(a, b)
    elif pheptoan == '/':
        try:
            print "Thuong la %f", chia(a, b)
        except Exception, e:
            print e
