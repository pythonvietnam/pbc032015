#!/usr/bin/python
# PCB032015
# tinh gia tri trung binh cua n so

L =[]

while True:
    a = raw_input("Nhap chuoi vao. An 'q' de thoat: ")
    if a == 'q':
        break
    else:
        if a.startswith("Chatmsg:"):
            L.append(a)
            
print "Cac chuoi dung yeu cau: ",L