#!/usr/bin/python
# PCB032015
# tinh gia tri trung binh cua n so

l = []

while True:
    a = raw_input("Nhap so, ket thuc bang 'over': ")
    try:
        if a == 'over':
            break
        b = float(a)
        l.append(b)
    except Exception, e:
        print "Ban da nhap sai, nhap vao 1 so!"
    
if len(l) == 0:
    print "Ban khong nhap vao chuoi nao"
else:
    print "Ket qua tinh trung binh cong cua %s la: %s" %(l, sum(l) / len(l))