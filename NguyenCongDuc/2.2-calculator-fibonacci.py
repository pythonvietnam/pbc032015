#!/usr/bin/python
# Chuong trinh tinh toan nhan / chia / cong / tru hai so
print "Chuong trinh tinh toan cong tru nhan chia 2 so tu nhien hoac viet day so Fibonacci!"
print "Nhap vao phep toan (cong / tru / nhan / chia / fibo), an 'q' de thoat!"

pheptoan = raw_input("Nhap phep toan: ")

try:
    a = int(raw_input("  > So thu nhat: "))
    b = int(raw_input("  > So thu hai: "))
except:
    print "Ban hay nhap vao mot so tu nhien!"
    
while pheptoan != 'q':
    if pheptoan == 'fibo':
        try:
            n = int(raw_input("Tinh day Fibonacci F(n), n= "))
        except:
            print "Ban hay nhap vao mot so tu nhien!"

        if n == 0:
            print "F(n) = 0"
        elif n == 1:
            print "F(n) = 1" 
        else:
            x = 0
            y = 1
            f = [0,1]
        for i in range(1,n):
            z = x + y
            x = y
            y = z
            f.append(z)
        print "Day F(%d) la: " %n, f

    elif pheptoan == 'cong' or pheptoan == '+':
        print "Tong 2 so la:", a + b
        break
    elif pheptoan == 'tru' or pheptoan == '-':
        print "Hieu 2 so la", a - b
        break
    elif pheptoan == 'nhan' or pheptoan == '*':
        print "Tich 2 so la ", a * b
        break
    elif pheptoan == 'chia' or pheptoan == '/':
        try:
            ketqua = a / float(b)
            print "Thuong 2 so la", ketqua
        except Exception, e:
            print e
        finally:
            break
    else:
        print "Ban hay nhap lai"
        pheptoan = raw_input("Nhap phep toan: ")
