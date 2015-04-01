#Dem ky tu trong chuoi
# import list;
from collections import Counter
print "----------- wellcome to program words counting ------------"
# lis []
space_count = 1
while True:
	try:
		str_c = raw_input("Ban nhap chuoi can dem : ")
		lis1 = []
		lis2 = []
		for i in str_c:
			if i.isspace():
				space_count = space_count + 1
			lis1.append(i)
		else:
			lis1.append('')
		lis2 = str_c.split()
		# print "List 2: ",lis2
		words_count = Counter()
		for w in lis2:
			words_count[w] +=1
		print "So tu trong chuoi:",space_count
		print "------------------------------------------------------------"
		print "So ky tu trong chuoi:", len(str_c)
		print "------------------------------------------------------------"
		print words_count
		print "------------------------------------------------------------"
		print "Danh sach chuoi vua nhap:", lis2
		break
	except ValueError:
		print " Loi khong xac dinh"
