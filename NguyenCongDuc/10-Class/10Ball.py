#!/usr/bin/python
# coding: utf-8
# ducnc92@hotmail.com
# Chuong trinh class

class ball:

    count = 0
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        ball.count += 1
        
    def bong_lan(self):
        print "Bong dang lan tai vi tri", self.x, self.y
        
    def bong_bay(self, z):
        self.z = z
        ball.count += 1
        print "Bong dang bay", z
    
    def dem_bong(self):
        print "Tong so bong", ball.count
    
in1 = ball(1,2,3)
in2 = ball(5,6,7)
#in1.bong_lan()
in1.dem_bong()

in1.h = 10

print in1.h

print "Co ton tai thuoc tinh ", hasattr(ball,'h')