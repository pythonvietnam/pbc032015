import os
os.system('clear')
print "---------------Chao mung ban den voi chuong trinh QLHS---------------"
lis1 = []
lis2 = []
lis3 = []
lis4 = []
dic1 = []
print 'Chon 1 de Nhap thong tin hoc sinh \n'
print "Chon 2 de In danh sach hoc sinh \n"
print "Chon 3 de Sap xep danh sach hoc sinh tang dan theo tuoi \n"
print "Chon Q de Thoat khoi chuong trinh \n"
Question1 = raw_input("Moi ban chon so:")
while True:
	try:
		if Question1 == "1":
			while True:
				try:
					full_name = raw_input("Nhap ho va ten hoc sinh:")
					if full_name == '':
						print "Ho va ten khong duoc trong"
						break
					else:
						lis1.append(full_name)	
					break
				except ValueError:
					print "Moi ban nhap dung thong tin hoc sinh"
			while True:
				try:
					age = int (raw_input("Nhap tuoi hoc sinh:"))
					# lis2 = age.split()
					lis2.append(age)
					break
				except ValueError:
					print "Moi ban nhap dung thong tin hoc sinh"
			while True:
				try:
					birthday = raw_input("Nhap ngay sinh hoc sinh:")
					# lis3 = birthday.split()
					lis3.append(birthday)
					break
				except ValueError:
					print "Moi ban nhap dung thong tin hoc sinh"
		if Question1 == "2" and len(lis1) ==0:
			print "Danh sach HS dang trong"
			break
		else:
			print "Thuc hien in danh sach"
			for i in range(len(lis1)):
				print "Ho va ten:",lis1[i],"----" "Tuoi:", lis2[i],"----" "Ngay sinh:",lis3[i]
		if Question1 == "3":
			lis4 = lis1 + lis2 + lis3
			for i in range(len(lis4)):
					# sorted(lis4)
				print "Danh sach tuoi tang dan",lis4
				# break
			# if Question2 == "1":
			# 	return True
	except ValueError:
		print "Nhap dung thong tin yeu cau"
