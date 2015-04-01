import sys
import math
print('Chao mung ban den voi may tinh python')
print('Ban go cong de thuc hien phep cong')
print('Ban go tru de thuc hien phep tru')
print('Ban go nhan de thuc hien phep nhan')
print('Ban go chia de thuc hien phep chia')
print('Ban go can de thuc hien phep can')
print('Ban go fi de hien thi day fibonacci')
c=raw_input('Ban muon lam phep toan nao ?')
if c=='cong':
	a=float(raw_input('Moi ban nhap vao so thu nhat:'))
	b=float(raw_input('Moi ban nhap vao so thu hai:'))
	print 'Ket qua phep tinh la', a+b
elif c=='tru':
	a=float(raw_input('Moi ban nhap vao so thu nhat:'))
	b=float(raw_input('Moi ban nhap vao so thu hai:'))
	print 'Ket qua phep tinh la', a-b
elif c=='nhan':
	a=float(raw_input('Moi ban nhap vao so thu nhat:'))
	b=float(raw_input('Moi ban nhap vao so thu hai:'))
	print 'Ket qua phep tinh la', a*b
elif c=='chia':
	a=float(raw_input('Moi ban nhap vao so thu nhat:'))
	b=float(raw_input('Moi ban nhap vao so thu hai:'))
	print 'Ket qua phep tinh la', a/b
elif c=='can':
	a=float(raw_input('Moi ban nhap vao so muon tinh can:'))
	print 'Ket qua phep tinh la',math.sqrt(a)
elif c=='fi':
	try:
		n=input('Moi ban nhap vao so n:')
		i=0
		j=1
		k=0
		print 'Day fibonacci tu 1 den ',n ,':'
		print i,
		print j,
		while k<=n:
			print i+j,
			k=i+j
			i=j
			j=k
	except:
		print("Ban phai nhap vao so")
else :
	print('Ban nhap chua dung phep toan')
	