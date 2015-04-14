#!/usr/bin/python

# Chuong trinh tinh toan nhan / chia / cong / tru hai so

from sys import argv
import calcmodule

print "Chuong trinh s 2 so tu nhien"

ten, x, y = argv

print 'Ket qua', calcmodule.cong(x,y)