#!/usr/bin/python

# Chuong trinh tinh toan nhan / chia / cong / tru hai so

print "Chuong trinh tinh toan cong tru nhan chia 2 so tu nhien"
print "Nhap vao phep toan (cong / tru / nhan / chia), an 'q' de thoat"

try:
    print "Nhap vao hai so:"
    a = int(raw_input("\t So thu nhat: "))
    b = int(raw_input("\t So thu hai: "))
except Exception, e:
    print e
    exit()

pheptoan = raw_input("Nhap phep toan: ")

if pheptoan == 'cong':
    print "Tong la:", a + b
elif pheptoan == 'tru':
    print "Hieu la", a - b
elif pheptoan == 'nhan':
    print "Tich la ", a * b
elif pheptoan == 'chia':
    try:
        print "Thuong la %f" %(a / float(b))
    except Exception, e:
        print e
elif pheptoan == 'q':
    exit()
else:
    print "Ban hay nhap lai"

print "ducnc"