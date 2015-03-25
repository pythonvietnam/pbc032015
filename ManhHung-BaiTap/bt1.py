import sys
import math
f = 0

name = raw_input('Hay cho biet ten cua ban? ')
if (name == 'loi' or name == 'Loi'):
	name = 'Thay giao'
	print "Xin, chao,",name,"muon lam phep tinh voi 2 so hay tinh so phi bo^ nan xi? hay chon: cong, tru, nhan, chia, fi"
else:	
	print "Xin chao,",name,"day la chuong trinh tinh lam phep tinh voi 2 so"
	print name,'muon lam phep tinh gi? cong, tru, nhan, chia: '
pt = raw_input()

if (pt == 'fi' and name == 'Thay giao'):
	print 'doi',name,'day tiep'
else:	
	print 'moi',name,'nhap so thu nhat: '
	x = float(input())
	print 'moi',name,'nhap so thu hai: '
	y = float(input())

	if pt == 'cong':
		kq = x + y
		print 'ket qua phep tinh', x, '+', y, '=', kq 
	if pt == 'tru':
		kq = x - y
		print 'ket qua phep tinh', x, '-', y, '=', kq
	if pt == 'nhan':
		kq = x * y
		print 'ket qua phep tinh', x, '*', y, '=', kq
	if pt == 'chia':
		kq = x / y
		print 'ket qua phep tinh', x, '/', y, '=', kq
	else:
		print 'chua hoc phep tinh',pt,'chiu ko biet ket qua'
