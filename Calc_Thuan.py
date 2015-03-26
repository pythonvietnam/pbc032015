calc = True 

while calc:
    print("1 = Cong")
    print("2 = Tru")
    print("3 = Nhan")
    print("4 = Chia")
    print("5 = Thoat")
    cmd = int(input("Chon phep tinh : "))
    if cmd == 1:
        print("Cong")
        a = int(input("Nhap so thu 1 :"))
        b = int(input("Nhap so thu 2 :"))
        print 'Ket qua: ', a + b
    elif cmd == 2:
        print("Tru")
        a = int(input("Nhap so thu 1 :"))
        b = int(input("Nhap so thu 2 :"))
        print 'Ket qua: ', a - b
    elif cmd == 3:
        print("Nhan")
        a = int(input("Nhap so thu 1 :"))
        b = int(input("Nhap so thu 2 :"))
        print 'Ket qua: ', a * b
    elif cmd == 4:
        print("Chia")
        a = int(input("Nhap so thu 1 :"))
        b = int(input("Nhap so thu 2 :"))
        print 'Ket qua: ', float(a) / b
    elif cmd == 5:
        print("Thoat!")
        calc = False
