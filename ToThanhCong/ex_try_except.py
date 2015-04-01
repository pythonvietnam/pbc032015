#!/bin/python 

try: 
    loichao = raw_input('Nhap loi chao: ')
except EOFError:
    print "Why did you do an EOF on me ?"
except KeyboardInterrupt:
    print "Ban da an thoat"
else:
    print "Nhap doan text {}" .format(loichao)

