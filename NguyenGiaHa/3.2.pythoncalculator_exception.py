#Python Calculator
print "Xin chao, day la chuong trinh Python Calculator"
running = True 
while running:
    print "----------------------------"
    print "1.Cong(+)"
    print "2.Tru(-)"
    print "3.Nhan(*)"
    print "4.Chia(/)"
    print "5.Fibonacci(f)"
    print "6.Quit(q)"
    answer = raw_input('Chon (1-6): ')

    if answer == "+" or answer == "1":
	 try: 
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a+b
	 except:
	     print 'Nhap sai!Hay thu lai.'
    elif answer == "-" or answer == "2":
	 try:  
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a-b
	 except:
	     print 'Nhap sai!Hay thu lai.'
    elif answer == "*" or answer == "3":
	 try: 
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a*b
	 except:
	     print 'Nhap sai!Hay thu lai.'
    elif answer == "/" or answer == "4":
	 try:
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     while b == 0:
         	     b = float(raw_input('So thu 2 phai khac 0, hay nhap lai: '))
	     print 'Ket qua: ', a/b
	 except:
	     print 'Nhap sai!Hay thu lai.'
    elif answer == "f" or answer == "5":
	 try:
	     n = int(raw_input('Tinh F(n), hay nhap n: '))
	     a=0
	     b=1
	     i=1
	     r=0
	     if n==0 or n==1:
		     r=n
	     else:
	       while i<n:
		     r=a+b
		     a=b
		     b=r
		     i=i+1
		     
	     print 'F('+str(n)+')= ', r
	 except:
	     print 'Nhap sai!Hay thu lai.'
    elif answer == "q" or answer == "6":
 	     running = False   
 	     print 'Quit!'
	


