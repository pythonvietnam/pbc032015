def cong (a,b):
	print("Ket qua phep cong la %d" %(a+b))	
def tru (a,b):
	print("Ket qua phep tru la %d" %(a-b))
def nhan (a,b):
	print("Ket qua phep nhan la %d" %(a+b))
def chia (a,b):
	print("Ket qua phep chia la %d" %(a/b))
def nhap ():
	a = int(input("Gia tri thu nhat :"))
	b = int(input("Gia tri thu hai :"))
print("Hello, I am Oanh\nThis is my Caculator program")	
print("What kind of math perform you want ?")
s = input("The math : ")
if s== "nhan":
	nhap()
	nhan(a,b)
elif s == "tru":	
	tru(int(input("Gia tri thu nhat :")),int(input("Gia tri thu hai :")))
elif s == "cong":	
	nhap()
	cong(a,b)
elif s == "chia":	
	nhap()
	chia(a,b)