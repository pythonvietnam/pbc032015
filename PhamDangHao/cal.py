import math
import os
print '------CHAO BAN DEN VOI CHUONG TRINH PYTHONCALCULATOR------'
print'''Nhap 1 de thuc hien phep cong
Nhap 2 de thuc hien phep tru 
Nhap 3 de thuc hien phep nhan 
Nhap 4 de thuc hien phep chia'''
print '----------------------------------------------------------' 
while True:
	a=(raw_input('Vui long chon phep toan ban muon thuc hien - Nhan Q de thoat'))
	if a =='q':
		print 'Ban vua nhap phim Q! Chuong trinh se thoat'
		break
	else:
		try:
			if a=='1':
				print '---Thuc hien phep cong---'
				so1=input('Nhap so thu nhat: ')
				so2=input('Nhap so thu hai: ')
				ketqua=so1+so2
				print 'Ket qua phep cong', ketqua
			elif a=='2':
				print '---Thuc hien phep tru---'
				so1=input('Nhap so thu nhat')
				so2=input('Nhap so thu hai')
				ketqua=so1-so2
				print 'Ket qua phep tru', ketqua
			elif a=='3':
				print '---Thuc hien phep nhan---'
				so1=input('Nhap so thu nhat')
				so2=input('Nhap so thu hai')
				ketqua=so1*so2
				print 'Ket qua phep nhan', ketqua
			elif a=='4':
				print '---Thuc hien phep chia---'
				so1=input('Nhap so thu nhat')
				so2=input('Nhap so thu hai')
				ketqua=float(so1)/so2
				print 'Ket qua phep chia', ketqua 
			else:
				print 'Ban vua nhap 1 gia tri khong phu hop! Vui long lam lai'
				
		except:
			print 'Vui long nhap 1 chu so, khong phai ky tu'
		

	
