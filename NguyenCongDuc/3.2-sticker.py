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

input = raw_input("Nhap vao sticker mong muon:")

while input != 'q':
    if input == '1':
        print ":)"
        break
    elif input == '2':
        print ":x"
        break
    elif input == '3':
        print ":D"
        break
    elif input == '4':
        print "=)"
        break
    elif input == '5':
        print ":P"
        break
    elif input == '6':
        print "T_T"
        break
    else:
        input=raw_input("Ban da nhap sai, nhap lai sticker: ")
    