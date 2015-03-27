# -*- coding: utf-8 -*-
so=input("Nhap vao so can tinh binh phuong: ")
bp=input("Nhap vao gia tri can so sanh: ")
if so*so==bp:
	print'Bang nhau roi'
elif so*so<bp:
	print 'Lon hon roi'
elif so*so>bp:
	print 'Nho hon roi'