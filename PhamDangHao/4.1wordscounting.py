oldstr=raw_input('Vui long nhap van ban: ')
new=oldstr
count=len(oldstr)
rep = ",:!.?;(""'')" #Khai bao cac ky tu dac biet nhu dau ., dau , hay dau ! trong cau thuong co de xoa cac ky tu do khoi chuoi
# vong lap de xoa cac ky tu dac biet trong chuoi
for j in range(0,len(rep)): 
	oldstr =oldstr.replace(rep[j],"")
mang={}
a=oldstr.split() # Ham split dung de tach 1 string thanh cac doan nho
if len(a)>0:
	for i in range(0,len(a)):
		if a[i] in mang:
			mang[a[i]]=mang[a[i]]+1
		else:
			mang[a[i]]=1
else:
	print 'Chuoi ban vua nhap khong co tu nao'
print "Ban vua nhap doan van ban: ",new,"Doan van ban nay co:",count,"ky tu"
for a[i] in mang:
	print'Tu',"'", a[i],"'",'da xuat hien ', mang[a[i]], 'lan'