#!/usr/bin/python
# -*- coding: utf-8 -*-
# PCB032015
# Chuong trinh quan ly sinh vien su dung list va dictionary
# List chua danh sach sinh vien, moi dictionary trong list la mot sinh vien voi key la id, ma, ten, diem
# ducnc92@hotmail.com

hello = '''\nChuong tring quan ly sinh vien!
Moi ban lua chon chuc nang:
\t1. Them sinh vien
\t2. Xoa sinh vien
\t3. Sua sinh vien 
\t4. Liet ke danh sach sinh vien
\t5. Thoat'''

list_sv = []

while True:

    print hello
    chucnang = raw_input("  > Ban lua chon: ")
    
    if chucnang == '5' or chucnang == 'q':
        print "Bye!"
        break
    
    elif chucnang == '1':
        i = len(list_sv) +1
        print ("\nChuc nang Them sinh vien")        
        ma_sv = raw_input("Nhap vao ma so sinh vien: ")
        ten_sv = raw_input("Nhap vao ten: ")
        
        # Nhap vao diem cua sv, kiem tra diem nhap vao co chinh xac hay khong
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
        for j in range(len(list_sv)):
            if ma_sv == list_sv[j]['ma']:
                print "\n => Fail! MaSV da ton tai!"
                flag = True
                break
        if flag == False:
            list_sv.append({'id' : i, 'ma' : ma_sv, 'ten' : ten_sv, 'diem': diem_sv})
            print "\n => Da nhap sinh vien thanh cong"
                
    elif chucnang == '2':
        print ("\nChuc nang xoa sinh vien")
        ma_sv = raw_input("  > Nhap ma sinh vien can xoa: ")
        
        # Tim MaSV trong danh sach va xoa sinh vien do
        flag = False
        for i in range(len(list_sv)):
            if ma_sv == list_sv[i]['ma']:
                del(list_sv[i])
                print "\n  => Da xoa sinh vien"
                flag = True
                break
        if flag == False:
            print "\n  => Khong ton tai sinh vien de xoa!"
            
            
    elif chucnang == '3':
        print ("\nChuc nang sua sinh vien")
        ma_sv = raw_input("  > Nhap ma sinh vien can sua: ")
        flag = False
        for i in range(len(list_sv)):
            if ma_sv == list_sv[i]['ma']:
                while True:
                    sua = raw_input("\Moi ban lua chon chuc nang:\n\t1. Sua ten\n\t2. Sua diem\n\tq. Quit!\n\t\t Ban chon: ")
                    if sua == '1':
                        ten = raw_input("  > Nhap ten moi: ")
                        list_sv[i]['ten'] = ten
                        print "\n => Da sua ten!"
                    elif sua == '2':
                        diem = raw_input("  > Nhap diem moi: ")
                        list_sv[i]['diem'] = diem
                        print "\n => Da sua diem!"
                    elif sua == 'q':
                        break
                print "\n => Da sua xong!"        
                break
        if flag == False:
            print "\n  => Khong ton tai sinh vien de sua!"
        print list_sv    
            
    elif chucnang == '4':
        print '''\n Chuc nang liet ke sinh vien
                 An 1 de sap xep theo MaSV
                 An 2 de sap xep theo Ten
                 An 3 de sap xep theo Diem tang dan
                 An 4 de sap xep theo Diem giam dan'''
                 
        press = raw_input("  > Nhap vao kieu sap xep: ")
        
        # Sap xep danh sach sinh vien theo yeu cau
        if press == '1':
            L = sorted(list_sv, key = lambda list_sv:list_sv['ma'])
        elif press == '2':
            L = sorted(list_sv, key = lambda list_sv:list_sv['ten'])
        elif press == '3':
            L = sorted(list_sv, key = lambda list_sv:list_sv['diem'])
        elif press == '4':
            L = sorted(list_sv, key = lambda list_sv:list_sv['diem'], reverse = True)
        else:
            print "\n  => Ban da chon sai chuc nang!"
        
        # In ra ket qua sau khi sap xep
        print '''\n\tMaSV\t|\tTenSV\t\t|\t\tDiem
\t----------------------------------------------------'''
        for i in range(len(L)):
            print '''\t%s\t|\t%s\t\t|\t\t%s''' %(L[i]['ma'], L[i]['ten'], L[i]['diem'])
        raw_input()            