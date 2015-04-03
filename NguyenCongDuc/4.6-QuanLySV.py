#!/usr/bin/python
# PCB032015
# Chuong trinh quan ly sinh vien
# ducnc92@hotmail.com

hello = '''\nChuong tring quan ly sinh vien!
Moi ban lua chon chuc nang:
\t1. Them sinh vien
\t2. Xoa sinh vien
\t3. Liet ke danh sach sinh vien
\t4. Thoat'''

list_sv = []

while True:

    print hello
    chucnang = raw_input("  > Ban lua chon: ")
    
    if chucnang == '4' or chucnang == 'q':
        print "Bye!"
        break
    
    
    elif chucnang == '1':
        print ("\nChuc nang Them sinh vien")
        ma_sv = raw_input("Nhap vao ma so sinh vien: ")
        
        ten_sv = raw_input("Nhap vao ten: ")
        
        while True:
            try: 
                diem_sv = float(raw_input("Nhap vao diem: "))
                if diem_sv < 0 or diem_sv > 10:
                    print "  => Fail! Diem la so tu 0 den 10"
                else:
                    break
            except:
                print "  => Fail! Ban hay nhap vao mot so la diem cua sinh vien!"
            
        # Kiem tra xem MaSV da ton tai hay chua, neu chua co se them sinh vien vao danh sach
        flag = False
        for i in range(len(list_sv)):
            if ma_sv == list_sv[i][0]:
                print "\n => Fail! MaSV da ton tai!"
                flag = True
                break
        if flag == False:
            list_sv.append((ma_sv, ten_sv, diem_sv))
            print "\n => Da nhap sinh vien thanh cong"
            
            
    elif chucnang == '2':
        print ("\nChuc nang xoa sinh vien")
        ma_sv = raw_input("  > Nhap ma sinh vien can xoa: ")
        
        # Tim MaSV trong danh sach va xoa sinh vien do
        flag = False
        for i in range(len(list_sv)):
            if ma_sv == list_sv[i][0]:
                del(list_sv[i])
                print "\n  => Da xoa sinh vien"
                flag = True
                break
        if flag == False:
            print "\n  => Khong ton tai sinh vien de xoa!"
            
            
    elif chucnang == '3':
        print '''\n Chuc nang liet ke sinh vien
                 An 1 de sap xep theo MaSV
                 An 2 de sap xep theo Ten
                 An 3 de sap xep theo Diem'''
                 
        press = raw_input("  > Nhap vao kieu sap xep: ")
        
        # Sap xep danh sach sinh vien theo yeu cau
        if press == '1':
            list_sv.sort(key = lambda list_sv:list_sv[0])
        elif press == '2':
            list_sv.sort(key = lambda list_sv:list_sv[1])
        elif press == '3':
            list_sv.sort(key = lambda list_sv:list_sv[2])
        else:
            print "\n  => Ban da chon sai chuc nang!"
        
        # In ra ket qua sau khi sap xep
        print '''\n\tMaSV\t|\tTenSV\t\t|\t\tDiem
\t----------------------------------------------------'''
        for i in range(len(list_sv)):
            print '''\t%s\t|\t%s\t\t|\t\t%s''' %(list_sv[i][0], list_sv[i][1], list_sv[i][2])
        raw_input()    