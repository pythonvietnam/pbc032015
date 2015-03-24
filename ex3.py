print("Hello, this is my program")
print("Ban muon thuc hien phem tinh gi ?")
s = input("phep toan thu hien : ")
if s== "nhan":
	print("moi ban nhap gia tri: ")
	a = int(input("Gia tri thu nhat :"))
	b = int(input("Gia tri thu hai :"))
	print("Ket qua la %d" % (a*b))
elif s == "tru":	
	print("moi ban nhap gia tri: ")
	a = int(input("Gia tri thu nhat :"))
	b = int(input("Gia tri thu hai :"))
	print("Ket qua la %d" % (a-b))
elif s == "cong":	
	print("moi ban nhap gia tri: ")
	a = int(input("Gia tri thu nhat :"))
	b = int(input("Gia tri thu hai :"))
	print("Ket qua la %d" % (a+b))
elif s == "chia":	
	print("moi ban nhap gia tri: ")
	a = int(input("Gia tri thu nhat :"))
	b = int(input("Gia tri thu hai :"))
	print("Ket qua la %d" % (a//b))
elif s == "Fib":
	print("Moi ban nhap gia tri:")
	n = int(input("Gia tri n :"))
	a,b =0,1
	while b< n:
		print(b,end =" ")
		c = a+b
		a =  b
		b = c 
	