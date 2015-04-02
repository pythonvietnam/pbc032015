print "-----Chuong trinh quan ly hoc sinh-----"
print "1. Them moi hoc sinh"
print "2. Danh sach hoc sinh"
print "3. Sap xep hoc sinh"
print "Q. Thoat chuong trinh"
qlhs=[]
while True:
	chon=raw_input("Vui long chon chuong trinh muon thuc hien: ")
	if chon =="1":
		print "---Them moi hoc sinh---"
		
		ten=raw_input('Nhap ho va ten: ')
		while True:
			try:
				tuoi=int(raw_input('Nhap tuoi: '))
				break
			except:
				print 'Vui long nhap lai tuoi la 1 so' 
		diachi=raw_input('Nhap dia chi: ') 
		hs=ten+':'+str(tuoi)+':'+diachi
		qlhs.append(hs)
	if chon=="2":
		print "---Danh sach hoc sinh---"
		print 'SBD','	Ho va ten 	','		tuoi 	','		dia chi 	'
		for i in range(0,len(qlhs)):
			tach=qlhs[i].split(':')
			print i,'	', tach[0],'			',tach[1],'			',tach[2]
	if chon=="3":
		print "---Sap xep danh sach hoc sinh---"
		print "1.Sap xep theo tuoi"
		print "2. Sap xep theo ten"
		order=raw_input("Vui long chon cach sap xep")
		if order=="1": 
			tuoi=sorted(qlhs,key=lambda x: (x.split(':')[1]))
			print 'SBD','	Ho va ten 	','	tuoi 	','		dia chi 	' 
			for i in range(0,len(qlhs)): 
				tach=tuoi[i].split(':')
				print i,'	', tach[0],'		',tach[1],'			',tach[2]
		elif order=="2":
			 
			ten=sorted(qlhs, key=lambda x: (x.split(':')[0]).split()[2]) 
			print 'SBD','	Ho va ten 	','		tuoi 	','		dia chi 	'
			for i in range(0,len(ten)): 
				tach=ten[i].split(':') 
				print i,'	', tach[0],'			',tach[1],'			',tach[2]
		
	if chon=='q':
		break
	 
	 