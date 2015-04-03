#!/usr/bin/python
# PCB032015
# tinh gia tri trung binh cua n so

string = "fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info"

a = string.split(":")
print "Nguoi gui: ", a[0]

b = a[1].split(".")
print "Noi dung: ", b[0]

c = a[1].split()
print "Nguoi nhan: ", c[6]
