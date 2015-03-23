#!/usr/bin/python
# Chuong trinh tinh toan nhan / chia / cong / tru hai so
print "Chuong trinh tinh toan cong tru nhan chia 2 so tu nhien hoac viet day so Fibonacci!"
print "Nhap vao phep toan (cong / tru / nhan / chia / fibo), an 'q' de thoat!"

print "Nhap vao hai so:"
a = int(raw_input("\t So thu nhat: "))
b = int(raw_input("\t So thu hai: "))

pheptoan = raw_input("Nhap phep toan: ")

while pheptoan != 'q':
    if pheptoan == 'cong':
        print "Tong 2 so la:", a + b
        break
    elif pheptoan == 'tru':
        print "Hieu 2 so la", a - b
        break
    elif pheptoan == 'nhan':
        print "Tich 2 so la ", a * b
        break
    elif pheptoan == 'chia':
        print "Thuong 2 so la", a / float(b)
        break
    elif pheptoan == 'fibo':
        d = int(raw_input("Nhap gioi han cua day fibonacci: "))
        x = 1
        y = 1
        z = 0
        while z < d:
            z = x + y
            x = y
            y = z
            if z >= d:
                exit()
            print z
        break
    else:
        print "Ban hay nhap lai"
        pheptoan = raw_input("Nhap phep toan: ")
