#!/usr/bin/python

from os.path import exists

file = raw_input ("Nhap vao duong dan file: ")

if exists(file):
    handle = open(file, 'r')
    i = 0
    for line in handle:
        i += 1
        print line.rstrip()
   
    print "So dong:", i
else:
    print "Khong ton tai file"