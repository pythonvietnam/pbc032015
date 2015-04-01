#!/bin/python

print "Moi ban nhap so: "
L = []
while True:
   nhapso = raw_input('Nhap so: ')
   try:
       if nhapso == 'over':
           break
       else:
           b = int(nhapso)
           L.append(b)
   except Exception, e:
       print "sai roi ong oi"
#
print ""
print L
print sum(L)/len(L)
print "bye bye"
