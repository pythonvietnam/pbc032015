#!/usr/bin/python
# PCB032015
# Chuong trinh doan so

try:
    a = int(raw_input("Nhap so thu 1: "))
    b = int(raw_input("Nhap so thu 2: "))
except:
    print "Nhap vao so!"
    exit()
if a**2 == b:
    print "Chinh xac, ban da doan dung!"
elif a**2 > b:
    print "Ban nhap so thu 2 qua nho!"
else:
    print "Ban nhap so thu 2 qua lon!"