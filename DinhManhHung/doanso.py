import sys
import math
print 'day la chuong trinh giup doan binh phuong cua 1 so'
so = input('nhap so can doan binh phuong ',)
bp = input('ban doan binh phuong cua so vua nhap la bao nhieu ',)
so = so * so
if bp == so:
	print 'ban da doan dung'
elif bp < so:
	print 'qua thap'
else:
	print 'qua cao'