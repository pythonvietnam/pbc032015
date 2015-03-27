#!/usr/bin/python
# PCB032015
# Dem so lan xuat hien cua mot tu, so lan xuat hien cua 1 ky tu trong mot chuoi nhap vao

print "Chuong trinh dem tu, dem ky tu!"
a = raw_input("\nNhap vao chuoi can dem: ")

#Chuyen string thanh cac list
list_word = a.split()
list_char = list(a)

#Khoi tao dictionary
dic_word = {}
dic_char = {}

#Dem so tu trong chuoi
for i in list_word:
    if i in dic_word:
        dic_word[i] = dic_word[i] + 1
    else:
        dic_word[i] = 1

#Chuyen dictionary thanh list de sap xep de in
l1 = dic_word.items()
l1.sort()

if len(l1) == 0:
    print "\nKhong co tu nao trong chuoi!"
else:
    print "\nSo lan xuat hien cua cac tu la:"
    for i in l1:
        print "  > Tu %s xuat hien %s lan" %(i[0], i[1]) 
        
#for key in dic_word:
#    print "Tu %s xuat hien %d lan " %(key,dic_word[key])

for j in list_char:
    if j in dic_char:
        dic_char[j] = dic_char[j] + 1
    else:
        dic_char[j] = 1

l2 = dic_char.items()
l2.sort() 
       
if len(l2) == 0:
    print "\nKhong co ky tu nao trong chuoi!"
else:
    print "\nSo lan xuat hien cua cac ky tu la: "
    for j in l2:
        print "  > Ky tu %s xuat hien %d lan" %(j[0], j[1]) 
