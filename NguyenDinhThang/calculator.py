import math

print " Calculator Python"

print "--------------------------------"

print "1.Cong(+)"

print "2.Tru(-)"

print "3.Nhan(*)"

print "4.Chia(/)"

print "Quit(q)"

# question = Y or y 

# while (question == Y or y):

running = True

while True:

	# Qes = raw_input ("Ban muon thuc hien chuong trinh Y/N") 

	# if Qes == "Y" or Qes == "y":

	# running = Trueraw_input

# while running:

# while (q == q):

		# try:

		# 	q = raw_input (" Nhap Q de thoat chuon

	try:

		pheptoan = str(raw_input ("Nhap phep toan:"))

		break		

	# else:

	# 	running = False

	# 	print " Quit!!"

	except ValueError:

		print " Loi nhap du lieu"

if pheptoan == "+" or pheptoan == "1":

	while True:	

		try:

			a = int(raw_input ("Nhap tham so a:"))

			break

		except ValueError:

			print "!----- Nhap du lieu dang so -----!"

	while True:

		try:

			b = int (raw_input ("Nhap tham so b:"))

			break

		except ValueError:

			print "!----- Nhap du lieu dang so -----!"

	print "Phep cong = ", a+b 

elif pheptoan == "-" or pheptoan =="2":

		while True:	

			try:

				a = int(raw_input ("Nhap tham so a:"))

				break

			except ValueError:

				print "!----- Nhap du lieu dang so -----!"

		while True:

			try:

				b = int (raw_input ("Nhap tham so b:"))

				break

			except ValueError:

				print "!----- Nhap du lieu dang so -----!"

		print "Phep tru = ", a-b 

elif pheptoan == "*" or pheptoan =="3":

		while True:	

			try:

				a = int(raw_input ("Nhap tham so a:"))

				break

			except ValueError:

				print "!----- Nhap du lieu dang so -----!"

		while True:

			try:

				b = int (raw_input ("Nhap tham so b:"))

				break

			except ValueError:

				print "!----- Nhap du lieu dang so -----!"

		print "Phep nhan = ", a*b 

elif pheptoan == "/" or pheptoan =="4":

		while True:	

			try:

				a = int(raw_input ("Nhap tham so a:"))

				break

			except ValueError:

				print "!----- Nhap du lieu dang so -----!"

		while True:

			try:

				b = int (raw_input ("Nhap tham so b:"))

				break

			except ValueError:

				print "!----- Nhap du lieu dang so -----!"

		print "Phep chia = ", a/float(b)

elif pheptoan == "q" or pheptoan == "Q":

		running = False

		print " Quit !"

else:

	print " Phep toan chon khong phu hop"	

	print "Phep Cong chon + hoac 1"

	print "Phep Tru chon - hoac 2"

	print "Phep Nhan chon * hoac 3"

	print "Phep Chia chon / hoac 4"
