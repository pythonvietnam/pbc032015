#python
#Chuong trinh quan ly hoc sinh
running = True
d={}
l=[]
i=0
try:
    while running:
        print '-----------------'
        print '1. Them hoc sinh'
        print '2. Tim kiem'
        print '3. Sua'
        print '4. Xoa'
        print '5. In'
        print '6. Thoat'
        
        answer = raw_input('Hay chon (1-5): ')
        if answer =='1':
            #Add
            d['id'] = len(l)
            d['hoten'] = raw_input('Ho ten hoc sinh: ')
            d['bod'] = raw_input('Ngay sinh (dd/mm/yyyy): ')
            d['lop'] = raw_input ('Lop: ')
            d['qq'] = raw_input('Que quan: ')
            l.append(d)
            d={}
            
        elif answer == '2':
            #Search
            s = raw_input('Ho ten hoc sinh can tim: ')
            c=0
            for i in range(len(l)):
                if l[i]['hoten']==s:
                    print str(l[i]['id'])+' '+l[i]['hoten']+' '+l[i]['bod']+' '+l[i]['qq']
                    c=c+1
            if c==0:
                print 'Khong tim thay, hay thu lai.' 
                
        elif answer == '3':
            #Modify
            s = input('Nhap id hoc sinh can sua: ')
            c=0
            for i in range(len(l)):
                if l[i]['id']==s:
                    d['id'] = s
                    d['hoten'] = raw_input('Ho ten hoc sinh: ')
                    d['bod'] = raw_input('Ngay sinh (dd/mm/yyyy): ')
                    d['lop'] = raw_input ('Lop: ')
                    d['qq'] = raw_input('Que quan: ')
                    l.remove(l[i])
                    l.insert(i,d)
                    c=c+1
                
            if c==0:
                print 'Khong tim thay, hay thu lai.' 
        elif answer == '4':
            #Del
            s = input('Nhap id hoc sinh can xoa: ')
            c=0
            for i in range(len(l)):
                if l[i]['id']==s:
                    l.remove(l[i])
                    c=c+1
            if c==0:
                print 'Khong tim thay, hay thu lai.' 
        elif answer == '5':
            
            for i in range(len(l)):
               print str(l[i]['id'])+' '+l[i]['hoten']+' '+l[i]['bod']+' '+l[i]['qq']
            #l.sort()
            #print l

        elif answer == '6':
            running = False
            print 'Quit!'
        
except:
        print 'Error occurred!'
finally:
        print 'Done!'
