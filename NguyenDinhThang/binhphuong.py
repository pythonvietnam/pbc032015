import math
while True:
    try:
        d =  str(raw_input("Ban co muon chay khong Y/N:"))
        break
        print "gia tri ",d
    except ValueError:
        print " oh oh he he"
while str(d) == y:
    print " Chao mung ban den chuong trinh"
    while True:
        try:
            a = input("Nhap so thu 1:")
            break
        except ValueError:
            print " Ban phai nhap so"
    b = input (" Nhap so thu 2:")
    c = a*a
    print "Binh phuong so 1 ",c
    if c == b:
        print " So ban nhap bang nhau"
    else:
        if c > b:
                print " So ban nhap qua cao"
        else:
            if c < b:
                    print " So ban nhap qua thap"
else:        
    print "Tam biet"
