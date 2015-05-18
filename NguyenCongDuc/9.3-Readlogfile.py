#!/usr/bin/python
# coding: utf-8
# ducnc92@hotmail.com
# Chuong trinh tim kiem log chat cua 1 thanh vien

#from sys import argv

handle = open('D:\Python\pbc032015\NguyenCongDuc\skype.pythonclass.log','r')
for line in handle:
    l = line.split('M] ')
    if len(l) > 1:
        print l[1]
    else:
        print l
#    print l[10:]