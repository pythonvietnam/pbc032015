#!/usr/bin/python
# ducnc92@hotmail.com
# Chuong trinh su dung 1 tu dien co san de giai nen mot file zip su dung mat khau

import zipfile
from sys import argv

def extract(line, i):
    try:
        try:
            z = zipfile.ZipFile(target)
        except:
            print "Ban nhap duong dan file zip khong dung!"
            exit()
            
        z.extractall(pwd = line)
        print "Mat khau dung la: ", line, "tai dong so ",i
        exit()
    except Exception, e:
        print "Dong so: ",i, "khong phai la mat khau!"

        
if __name__ == '__main__':

    if len(argv) != 3:
        print '''Chuong trinh yeu cau 3 tham so.
Su dung cu phap 'python 9.2-zipfile.py file_zip file_tu_dien' de tien hanh giai ma'''
        exit()

    script, target, dict = argv
    
    try:
        handle = open(dict,'r')
    except:
        print "Ban nhap duong dan file tu dien khong dung!"
        exit()
    i = 0
    for line in handle:
        i += 1
        line = str(line.strip())
        extract(line, i)
        
    print "Mat khau dung la: ", line, "tai dong so", i    
