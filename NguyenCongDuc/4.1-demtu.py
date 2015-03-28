#!/usr/bin/python
# PCB032015
# Dem so lan xuat hien cua mot tu

print "Chuong trinh dem tu"

d = {}

for i in range(1,11):
    a = raw_input("Nhap lan so:")
    if a in d:
        d[a] = d[a] + 1
    else:
        d[a] = 1
        
for key in d:
    print "Tu %s xuat hien %d lan " %(key,d[key])
