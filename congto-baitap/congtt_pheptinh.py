#!/bin/python

print "XIN CHAO. Day la chuong trinh may tinh"
print "Nhap phep tinh voi cac lua chon: cong, tru, nhan, chia"
#
a = int(raw_input("So thu nhat: "))
b = int(raw_input("So thu hai: "))
print ""
#
pheptinh = raw_input("Phep tinh: ")

#
if pheptinh == "cong":
   print "a + b = ", a + b

if pheptinh == "tru":
   print "a - b = ", a - b

if pheptinh == "nhan":
   print "a x b =", a * b

if pheptinh == "chia":
   print "a : b = ", float(a)/float(b)     
    
