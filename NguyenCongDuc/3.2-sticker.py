#!/usr/bin/python
# PCB032015
# Chuong trinh hien thi sticker!

print "Chuong trinh hien thi sticker!"

print '''Cac Sticker he thong ho tro:
\t1: :)
\t2: :x
\t3: :D
\t4: =)
\t5: :P
\t6: T_T 
\tq: quit'''

xxx = raw_input("Nhap vao sticker mong muon: ")

while xxx != 'q':
    if xxx == '1':
        print ":)"
        break
    elif xxx == '2':
        print ":x"
        break
    elif xxx == '3':
        print ":D"
        break
    elif xxx == '4':
        print "=)"
        break
    elif xxx == '5':
        print ":P"
        break
    elif xxx == '6':
        print "T_T"
        break
    else:
        xxx=raw_input("Ban da nhap sai, nhap lai sticker: ")
    