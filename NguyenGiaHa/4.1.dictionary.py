print 'Dem so lan xuat hien cua cac tu trong 10 lan nhap.'
d = {}
for i in range(1,11):
    a=raw_input("Nhap lan "+str(i)+" : ")
    if a in d:
        d[a] = d[a]+1
    else:
        d[a] = 1
print 'Ki tu '+str(a)+' da xuat hien '+d[a]+' lan.'
#print d
#for key in d:
#    print 'Ki tu '+key+' da xuat hien '+d[key]+' lan.'
