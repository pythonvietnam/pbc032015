#!/usr/bin/python
# -*- coding: utf-8 -*-
# PCB032015
# Chuong trinh quan ly sinh vien su dung database 
# CREATE TABLE SinhVien(ID int NOT NULL AUTO_INCREMENT, MaSV varchar(255) NOT NULL, TenSV varchar(255) NOT NULL, Diem int(10), PRIMARY KEY (ID))
# ducnc92@hotmail.com

from database import SqlDB
from sys import argv

hello = '''\nChuong tring quan ly sinh vien!
Moi ban lua chon chuc nang:
\t1. Them sinh vien
\t2. Xoa sinh vien
\t3. Sua sinh vien 
\t4. Tim kiem sinh vien
\t5. Liet ke danh sach sinh vien
\t6. Thoat'''

sv = SqlDB()

# Ham them sinh vien
def them_sv():
    '''
    Day la ham dung de them sinh vien vao danh sach
    '''
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

    sql = "INSERT INTO SinhVien (MaSV, TenSV, Diem) VALUES (%s, %s, %s)"
    data2insert = (ma_sv, ten_sv, diem_sv)
    sv.InsertData(sql, data2insert)
    print "\n => Da nhap sinh vien thanh cong"
            

# Ham xoa sinh vien
def xoa_sv():
    '''
    Day la ham dung de xoa sinh vien trong danh sach
    '''
    print ("\nChuc nang xoa sinh vien")
    ma_sv = raw_input("  > Nhap ma sinh vien can xoa: ")
        
    # Tim MaSV trong danh sach va xoa sinh vien do
    try:
        sql = "DELETE FROM SinhVien WHERE MaSV = '%s'" %ma_sv
        sv.UpdateData(sql)
    except Exception,e:
        print "\n  => Khong ton tai sinh vien de xoa!"
        
def tim_sv():
    '''
    Day la ham dung de tim kiem sinh vien trong danh sach theo ten
    '''
    print ("\nChuc nang tim kiem sinh vien")
    list_sv = []
    ten_sv = raw_input("  > Nhap ten sinh vien can tim: ")
    data = sv.SelectData('select * from SinhVien')
    
    for i in range(len(data)):
        if data[i][2].startswith(ten_sv):
            list_sv.append(data[i])

    if len(list_sv) == 0:
        print "  => Khong tim thay sinh vien!"
    else:
            print '''\n\tMaSV\t|\tTenSV\t\t|\t\tDiem
\t----------------------------------------------------'''
            for i in range(len(list_sv)):
                print '''\t%s\t|\t%s\t\t|\t\t%s''' %(list_sv[i][1], list_sv[i][2], list_sv[i][3])
            raw_input()            

        
def sua_sv():
    '''
    Day la ham dung de sua thong tin 1 sinh vien trong danh sach
    '''
    print ("\nChuc nang sua sinh vien")
    ma_sv = raw_input("  > Nhap ma sinh vien can sua: ")
    while True:
        sua = raw_input("\Moi ban lua chon chuc nang:\n\t1. Sua ten\n\t2. Sua diem\n\t3. Sua ma sv\n\tq. Quit!\n\t\t Ban chon: ")
        if sua == '1':
            ten = raw_input("  > Nhap ten moi: ")
            sv.UpdateData("UPDATE SinhVien SET TenSV = '%s' WHERE MaSV = '%s'" %(ten, ma_sv))
            print "\n => Da sua ten!"
        elif sua == '2':
            diem = raw_input("  > Nhap diem moi: ")
            sv.UpdateData("UPDATE SinhVien SET Diem = '%s' WHERE MaSV = '%s'" %(diem, ma_sv))
            print "\n => Da sua diem!"
        elif sua == '3':
            ma = raw_input("  > Nhap ma sinh vien moi: ")
            sv.UpdateData("UPDATE SinhVien SET MaSV = '%s' WHERE MaSV = '%s'" %(ma, ma_sv))
            print "\n => Da sua ma sinh vien!"
        elif sua == 'q':
            break

#    if flag == False:
#        print "\n  => Khong ton tai sinh vien de sua!"


def in_sv():
    print '''\n Chuc nang liet ke sinh vien
    An 1 de sap xep theo MaSV
    An 2 de sap xep theo Ten
    An 3 de sap xep theo Diem tang dan'''
                 
    press = raw_input("  > Nhap vao kieu sap xep: ")
    
    data = sv.SelectData('select * from SinhVien')
    
    list_sv = []
    for i in range(len(data)):
        list_sv.append(data[i])
        
    # Sap xep danh sach sinh vien theo yeu cau
    if press == '1':
        list_sv.sort(key = lambda list_sv:list_sv[1])
    elif press == '2':
        list_sv.sort(key = lambda list_sv:list_sv[2])
    elif press == '3':
        list_sv.sort(key = lambda list_sv:list_sv[3])
    else:
        print "\n  => Ban da chon sai chuc nang!"

        # In ra ket qua sau khi sap xep
    print '''\n\tMaSV\t|\tTenSV\t\t|\t\tDiem
\t----------------------------------------------------'''
    for i in range(len(list_sv)):
        print '''\t%s\t|\t%s\t\t|\t\t%s''' %(list_sv[i][1], list_sv[i][2], list_sv[i][3])
    raw_input()            
    
while True:
    print hello
    chucnang = raw_input("  > Ban lua chon: ")
    
    if chucnang == '6' or chucnang == 'q':
        print "Bye!"
        break
    
    elif chucnang == '1':
        them_sv()
                
    elif chucnang == '2':
        xoa_sv()
            
    elif chucnang == '3':
        sua_sv()
        
    elif chucnang == '4':
        tim_sv()
        
    elif chucnang == '5':
        in_sv()
