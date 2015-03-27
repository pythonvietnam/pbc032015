#!/bin/python

print "XIN CHAO. Day la chuong trinh may tinh"
print "Nhap phep tinh voi cac lua chon: cong, tru, nhan, chia"
#


#
while 1:
    pheptinh = raw_input("Phep tinh: ")
    a = int(raw_input("So thu nhat: "))
    b = int(raw_input("So thu hai: "))
    print ""   
#
    if pheptinh == "cong":
        print "a + b = ", a + b

    elif pheptinh == "tru":
        print "a - b = ", a - b

    elif pheptinh == "nhan":
        print "a x b =", a * b

    elif pheptinh == "chia":
        print "a : b = ", float(a)/float(b)     
    else:
        break
print "bye bye"


