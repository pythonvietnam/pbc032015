#Dem ky tu trong chuoi
# import list;
from collections import Counter
print "----------- wellcome to program words counting ------------"
# lis []
demtu = 0
while True:
	try:
		str_c = raw_input("Ban nhap chuoi can dem : ")
		lis1 = []
		lis2 = []
		for i in str_c:
			if not i.isspace():
				lis1.append(i)
		lis2 = str_c.split()
		# Dem tu trong mot lis2
		words_count = 0
		for i in lis2:
			words_count = words_count +1
		# print "List 2: ",lis2
		# Dem so lan lap cua 1 tu trong lis2 
		words_count_seq = Counter()
		for w in lis2:
			words_count_seq[w] +=1
		print "So tu trong chuoi:",words_count
		print "------------------------------------------------------------"
		# Ham len lay do dai ky tu cua 1 chuoi
		print "So ky tu trong chuoi:", len(str_c)
		print "------------------------------------------------------------"
		print words_count_seq
		print "------------------------------------------------------------"
		print "Danh sach chuoi vua nhap:", lis2
		break
	except ValueError:
		print " Loi khong xac dinh"
