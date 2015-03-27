import math
try:
    # d =  str(raw_input("Ban co muon chay khong Y/N:"))    
    # y = True
    # while str(d) = y:
    #     print " Chao mung ban den chuong trinh"
    while True:
        try:
            a = int(raw_input("Nhap so thu 1:"))
            break
        except ValueError:
            print " !----- Du lieu nhap dang so -----!"
        
    while True:
        try:
            b = int(raw_input("Nhap so thu 2:"))
            break
        except ValueError:
            print " !----- Du lieu nhap dang so -----!"
    c = a*a
    print "Binh phuong thu 1 ",c
    if c == b:
            print " So ban nhap bang nhau"
    elif c > b:
            print " So ban nhap qua cao"
    elif c < b:
                    print " So ban nhap qua thap"
    # else:        
    #     print "Tam biet"
except ValueError:
    print " Loi khong xac dinh"
finally:
    print "Done!"
