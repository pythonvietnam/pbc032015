import math
import os
print '------CHAO BAN DEN VOI CHUONG TRINH PYTHONCALCULATOR------'
print'''Nhap 1 de thuc hien phep cong
Nhap 2 de thuc hien phep tru 
Nhap 3 de thuc hien phep nhan 
Nhap 4 de thuc hien phep chia
Nhap 5 de tinh so fibonaci'''
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
elif a==5:
	print '---Tinh so Fibonaci---'
	fi=int(input('Vui long nhap so N:  '))
	a=0;b=1
	while a<fi:
		print a #in ra chuoi so fibo
		c = a+b #Gan gia tri C la gia tri trung gian tinh tong cua a va b
		a = b
		b = c 
else:
	print 'Ban vua nhap 1 gia tri khong phu hop! Vui long lam lai'