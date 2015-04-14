#!/usr/bin/python
# -*- coding: utf-8 -*-
# PCB032015
# Chuong trinh tinh luong 
# ducnc92@hotmail.com

hello = '''\nChuong trinh tinh luong!
Moi ban lua chon chuc nang:
\t1. Tinh luong
\t2. Thoat'''

def tinhluong(a, c, e, f , b = 400, d = 1.5):
    return (a * b) + (c * d) - e - f
     
    
while True:
    print hello
    
    chucnang = raw_input("  > Ban lua chon: ")
    
    if chucnang == '1':
        a = int(raw_input("Nhap vao he so luong: "))
        b = int(raw_input("Nhap vao luong co ban: "))
        c = int(raw_input("Nhap vao so gio lam them: "))
        d = int(raw_input("Nhap vao he so lam them: "))
        e = int(raw_input("Nhap vao bao hiem: "))
        f = int(raw_input("Nhap vao phi cong doan: "))
        print "Luong cua ban la: ", tinhluong (a, c, e, f, b = 400, d = 1.5)
#        print ketqua
        
    elif chucnang == '2' or chucnang == 'q':
        exit()
     