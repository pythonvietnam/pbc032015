#!/usr/bin/python
# PCB032015
# sap xep mot dictionary

D = {1:2, 3:4, 'a':'f', 'c':'d'}

print D

L = D.items()

L.sort()

print L

L1 = []

for (key, val) in D.items():
    (key,val) = (val,key)
    L1.append((key,val))

L1.sort()
print L1
