import math
import os
print '------CHAO BAN DEN VOI CHUONG TRINH PYTHONCALCULATOR------'
print'''Nhap 1 de thuc hien phep cong
Nhap 2 de thuc hien phep tru 
Nhap 3 de thuc hien phep nhan 
Nhap 4 de thuc hien phep chia'''
print '----------------------------------------------------------'
a=int(raw_input('Vui long chon phep toan ban muon thuc hien'))
os.system('cls') #0
if a==1:
	print '---Thuc hien phep cong---'
	so1=float(raw_input('Nhap so thu nhat'))
	so2=float(raw_input('Nhap so thu hai'))
	ketqua=so1+so2
	print 'Ket qua phep cong';print ketqua
elif a==2:
	print '---Thuc hien phep tru---'
	so1=float(raw_input('Nhap so thu nhat'))
	so2=float(raw_input('Nhap so thu hai'))
	ketqua=so1-so2
	print 'Ket qua phep tru';print ketqua
elif a==3:
	print '---Thuc hien phep nhan---'
	so1=float(raw_input('Nhap so thu nhat'))
	so2=float(raw_input('Nhap so thu hai'))
	ketqua=so1*so2
	print 'Ket qua phep nhan';print ketqua
elif a==4:
	print '---Thuc hien phep chia---'
	so1=float(raw_input('Nhap so thu nhat'))
	so2=float(raw_input('Nhap so thu hai'))
	ketqua=so1/so2
	print 'Ket qua phep chia';print ketqua
else:
	print 'Ban vua nhap 1 gia tri khong phu hop! Vui long lam lai'