print "-----Chuong trinh quan ly hoc sinh-----"
print "1. Them moi hoc sinh"
print "2. Danh sach hoc sinh"
print "3. Sap xep hoc sinh"
print "4. Sua hoc sinh"
print "Q. Thoat chuong trinh"
qlhs=[]
st=[]
while True:
	chon=raw_input("Vui long chon chuong trinh muon thuc hien: ")
	if chon =="1": 
		print "---Them moi hoc sinh---" 
		while True:
			try:
				ten=raw_input('Nhap ho va ten: ')
				if ten!='':
					break
			except:
				print 'loi roi'

		while True:
			try:
				tuoi=int(raw_input('Nhap tuoi: '))
				break
			except:
				print 'Vui long nhap lai tuoi la 1 so' 
		diachi=raw_input('Nhap dia chi: ')
		sb=len(st)
		hs={'id':sb+1,'hoten':ten,'tuoi':tuoi,'diachi':diachi}  
		st.append(hs) 
	if chon=="2":
		print "-----DANH SACH HOC SINH-----"
		print 'ID','	Ho va ten','	tuoi','	dia chi 	'
		for j in range(0,len(st)): 
				print st[j]['id'],'	',st[j]['hoten'],'	',st[j]['tuoi'],'	',st[j]['diachi']
	if chon=="3": 
		print '1. Sap xep tuoi tang dan'
		print '2. Sap xep tuoi gian dan'
		print '3. Sap xep ten tang dan'
		print '4. Sap xep ten giam dan'
		sx=raw_input('Vui long chon thu tu sap xep: ')
		# Sap xep tuoi tang dan
		if sx=="1":
			tuoi=sorted(st, key=lambda x:x['tuoi'])
			print 'ID','	Ho va ten','	tuoi','	dia chi 	'
			for j in range(0,len(tuoi)): 
				print tuoi[j]['id'],'	',tuoi[j]['hoten'],'	',tuoi[j]['tuoi'],'	',tuoi[j]['diachi']
		# sap xep tuoi giam dan 
		elif sx=="2":
			tuoi=sorted(st, key=lambda x:x['tuoi'], reverse=True)
			print 'ID','	Ho va ten','	tuoi','	dia chi 	'
			for j in range(0,len(tuoi)): 
				print tuoi[j]['id'],'	',tuoi[j]['hoten'],'	',tuoi[j]['tuoi'],'	',tuoi[j]['diachi']
		# Sap xep ten tang dan
		elif sx=="3": 
			tuoi=sorted(st, key=lambda x:x['hoten'].split()[len(x['hoten'].split())-1].lower)
			print 'ID','	Ho va ten','	tuoi','	dia chi 	'
			for j in range(0,len(tuoi)): 
				print tuoi[j]['id'],'	',tuoi[j]['hoten'],'	',tuoi[j]['tuoi'],'	',tuoi[j]['diachi']
		#Sap xep ten giam dan
		elif sx=="4": 
			tuoi=sorted(st, key=lambda x:x['hoten'].split()[len(x['hoten'].split())-1].lower, reverse=True)
			print 'ID','	Ho va ten','	tuoi','	dia chi 	'
			for j in range(0,len(tuoi)): 
				print tuoi[j]['id'],'	',tuoi[j]['hoten'],'	',tuoi[j]['tuoi'],'	',tuoi[j]['diachi']
	if chon=='4':
		print '---Sua thong tin hoc sinh---' 
		print 'ID','	Ho va ten','	tuoi','	dia chi 	'
		for j in range(0,len(st)): 
				print st[j]['id'],'	',st[j]['hoten'],'	',st[j]['tuoi'],'	',st[j]['diachi']
		while True: 
			try:
				ms=input('Nhap ID hoc sinh can sua: ') 
				test=st[ms-1]
				break
			except:
				print 'Khong co hoc sinh nay! Vui long kiem tra lai ID' 
		sbd=ms-1
		print st[sbd]['id'],'	',st[sbd]['hoten'],'	',st[sbd]['tuoi'],'	',st[sbd]['diachi']
		ten=raw_input('Nhap ten moi! Nhan enter de bo qua: ')
		tuoi=input('Nhap tuoi moi! Nhan enter de bo qua: ')
		diachi=raw_input('Nhap dia chi moi! Nhan enter de bo qua')
		if ten=='':
			ten=st[sbd]['hoten']
		else:
			ten=ten 
		if tuoi=='':
			tuoi=st[sbd]['tuoi']
		else:
			tuoi=tuoi
		if diachi=='':
			diachi=st[sbd]['diachi']
		else:
			diachi=diachi
		st[sbd]={'id':ms,'hoten':ten,'tuoi':tuoi,'diachi':diachi}
	if chon=='q':
		print 'Ban vua nhan phim Q. Chuong trinh tu dong thoat'
		break

