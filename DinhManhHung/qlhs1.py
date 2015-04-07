import os
import time
l=[]
ID=1
z=1
os.system('clear')
while True:
	print 'CHUONG TRINH QUAN LY HOC SINH:\n 1. Them hoc sinh \n 2. Danh sach hoc sinh \n 3. Sap xep danh sach hoc sinh \n 4. Tim thong tin hoc sinh \n 5. Sua thong tin hoc sinh \n 6. Thoat khoi chuong trinh'
	opt=raw_input('Chon: ')
	if opt=='6':
		os.system('clear')
		break
	elif opt=='1':
		os.system('clear')
		while opt=='1':
			print 'Nhap thong tin hoc sinh:'
			ht=raw_input('Ho ten: ')
			n=1
			while n==1:
				try: 
					ns=int(raw_input('Nam sinh: '))
					n=0
				except Exception, e:
					n=1
					#print e
					print 'Hay nhap dung nam sinh dang so nguyen'
			lop=raw_input('Lop: ')
			while True: 
				luu=raw_input('Luu thong tin hoc sinh? (y/n) ',)
				if luu=='y':
					l.append({'ID':ID,'Ho ten':ht,'Nam sinh':ns,'Lop':lop})
					ID=ID+1
					break
				elif luu=='n':
					break
			#ham check tiep tuc
			while True:		
				q=raw_input('Them hoc sinh khac? (y/n)')
				if q=='y':
					os.system('clear')
					break
				elif q=='n':
					opt='opt'
					os.system('clear')
					break
	elif opt=='2':
		os.system('clear')
		print 'DANH SACH HOC SINH'
		print '----------------------------------------------------------------------------'
		for i in l:
			print i
			print '----------------------------------------------------------------------------'
		#for i in sorted(l, key=lambda l:l['Ho ten']):
			#print i
	elif opt=='3':
		os.system('clear')
		while opt=='3':
			while True:	
				print 'Sap xep danh sach hoc sinh theo:\n 1. Ho ten\n 2. Tuoi giam dan\n 3. Tuoi tang dan\n 4. Lop\n x. Ve menu chinh'
				sort=raw_input('Chon: ',)
				if sort=='1':
					os.system('clear')
					print 'SAP XEP THEO HO TEN'
					for i in sorted(l, key=lambda l:l['Ho ten']):
						print i
				elif sort=='2':
					os.system('clear')
					print 'TUOI GIAM DAN'
					for i in sorted(l, key=lambda l:l['Nam sinh']):
						print i
				elif sort=='3':
					os.system('clear')
					print 'TUOI TANG DAN'
					for i in sorted(l, key=lambda l:l['Nam sinh'],reverse=True):
						print i
				elif sort=='4':
					os.system('clear')
					print 'SAP XEP THEO LOP'
					for i in sorted(l, key=lambda l:l['Lop']):
						print i
				elif sort=='x':
					opt='opt'
					os.system('clear')
					break
				else:
					print 'Ban chon khong dung, Hay chon lai'

	elif opt=='4':
		while opt=='4':
			os.system('clear')
			search=raw_input('Nhap ho ten hoc sinh can tim: ')
			while True:
				kq=0
				for i in l:
					if str.lower(i['Ho ten'])==str.lower(search):
						print i
						kq=1
					if kq!=1:
						os.system('clear')
						print 'Khong co thong tin hoc sinh:',search	
				search=raw_input('Nhap \'x\' de thoat, Hoac ho ten hoc sinh can tim: ')
				if search=='x':
					opt='opt'
					os.system('clear')
					break
	elif opt=='5':
		loi=0
		while opt=='5':
			n=1
			while n==1:
				os.system('clear')
				if loi==1:
					print 'ID ban nhap ko dung, Hay thu lai'
				print 'DANH SACH HOC SINH'
				print '----------------------------------------------------------------------------'
				for i in l:
					print i
					print '----------------------------------------------------------------------------'
				edit=raw_input('Nhap ID hoc sinh can sua hoac \'x\' de ve menu chinh: ')
				if edit=='x':
					opt='opt'
					os.system('clear')
					n=0
					break
				else:
					try:
						edit=int(edit)
						d=l[edit-1]
						ID1=d['ID']
						ht=d['Ho ten']
						ns=d['Nam sinh']
						lop=d['Lop']
						print 'Ho ten [',ht,']: '
						ht1=raw_input()
						if ht1!='':
							d['Ho ten']=ht1
						chk=1
						while chk==1: 
							try:
								print 'Nam sinh [',ns,']: '
								ns1=raw_input()
								if ns1!='':
									d['Nam sinh']=int(ns1)
								chk=0
							except Exception ,e:
								#print e
								print 'Hay nhap dung nam sinh dang so nguyen'
						print 'Lop [',lop,']: '
						lop1=raw_input()
						if lop1!='':
							d['Lop']=lop1
						while True: 
							luu=raw_input('Luu thong tin hoc sinh? (y/n) ',)
							if luu=='y':
								l[edit-1]=d
								break
							elif luu=='n':
								break
						loi=0
					except Exception, e:
						loi=1
						

	else:
		print 'Ban chon khong dung, Hay chon lai'
		time.sleep(1)
		os.system('clear')
print 'Chuong trinh se thoat trong giay lat'
time.sleep(1)
os.system('clear')