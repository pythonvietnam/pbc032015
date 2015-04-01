#!/bin/python

#day4
demtu = {}
for i in range(1,11):
    nhapvao = raw_input("Nhap tu: ")
    if nhapvao in demtu:
        demtu[nhapvao] = demtu[nhapvao] + 1
    else: 
        demtu[nhapvao] = 1
print demtu
#
print ""
#
for tukhoa in demtu:
    print "Ky tu \t", tukhoa,  "\tda co \t",  demtu[tukhoa]
