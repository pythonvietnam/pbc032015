#!/usr/bin/python

# Chuong trinh tinh toan nhan / chia / cong / tru hai so

print "Chuong trinh tinh toan cong tru nhan chia 2 so tu nhien"
print "Nhap vao phep toan (cong / tru / nhan / chia), an 'q' de thoat"

#def nhap2so:
print "Nhap vao hai so:"
a = int(raw_input("\t So thu nhat: "))
b = int(raw_input("\t So thu hai: "))

pheptoan = raw_input("Nhap phep toan: ")

if pheptoan == 'cong':
#    nhap2so()
    print "Tong la:", a + b
elif pheptoan == 'tru':
#    nhap2so()
    print "Hieu la", a - b
elif pheptoan == 'nhan':
#    nhap2so()
    print "Tich la ", a * b
elif pheptoan == 'chia':
#    nhap2so()
    print "Thuong la %f" %(a / b)
elif pheptoan == 'q':
    exit()
else:
    print "Ban hay nhap lai"
