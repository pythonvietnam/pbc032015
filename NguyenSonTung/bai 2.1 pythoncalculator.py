
running = True
print 'Xin chao,day la Python Calculator \n' 

while running:
	print 'Bat dau :\n'
	print '1 = +'
	print '2 = -'
	print '3 = x'
	print '4 = /'
	print '5 = quit \n'
 	
	lenh = int(input('Phep tinh muon thuc hien :  '))
 	
	if lenh == 1:
		print ("Phep cong \n")
		a = int(input('a :'))
		b = int(input('b :'))
		kq = a + b
		print a ,' + ', b,' = ', kq
		print '\n'
	elif lenh == 2:
		print 'Phep tru : \n'
		a = int(input('a :'))
		b = int(input('b :'))
		kq = a - b
		print a,'-',b,'=',kq
		print '\n'
	elif lenh == 3:
		print 'Phep nhan : \n'
		a = int(input('a :'))
		b = int(input('b :'))
		kq = a * b
		print a,'x',b,'=',kq
		print '\n'
	elif lenh == 4:
		print 'Phep chia : \n'
		a = int(input('a :'))
		b = int(input('b :'))
		kq =	a / b
		print a,'/',b,'=',kq
		print '\n'
	elif lenh == 5:
		running = False
