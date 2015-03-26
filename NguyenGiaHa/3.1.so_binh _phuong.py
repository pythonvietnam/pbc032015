import math
a = int(raw_input('Nhap a: '))
b = int(raw_input('Nhap binh phuong cua a: '))
if b == a*a:
    print 'Chinh xac!'
elif b>a*a:
    print 'So binh phuong ban nhap vao qua cao!'
else:
    print 'So binh phuong ban nhap vao qua thap!'
