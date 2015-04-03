#python
#Chuong trinh quan ly hoc sinh
running = True
d={}
try:
    while running:
        print '-----------------'
        print '1. Them hoc sinh'
        print '2. Tim kiem'
        print '3. Sua'
        print '4. Xoa'
        print '5. Thoat'
        
        answer = raw_input('Hay chon (1-5): ')
        if answer =='1':
            #Add
            hoten = raw_input('Ho ten hoc sinh: ')
            bod = raw_input('Ngay sinh (dd/mm/yyyy): ')
            lop = raw_input ('Lop: ')
            quequan = raw_input('Que quan: ')
            d[hoten] = [bod,lop,quequan]
        elif answer == '2':
            #Search
            s = raw_input('Ho ten hoc sinh can tim: ')
            if s in d:
                print 'Ho va ten: '+s
                print 'Ngay sinh: '+d[s][0]
                print 'Ngay sinh: '+d[s][1]
                print 'Que quan: '+d[s][2]
            else:
                print 'Khong tim thay, hay thu lai.'
        elif answer == '3':
            #Modify
            s = raw_input('Ho ten hoc sinh can sua: ')
            if s in d:
                print 'Ho va ten: '+s
                bod = raw_input('Ngay sinh (dd/mm/yyyy): ')
                lop = raw_input ('Lop: ')
                quequan = raw_input('Que quan: ')
                d[hoten] = [bod,lop,quequan]
                
            else:
                print 'Khong tim thay, hay thu lai.'
        elif answer == '4':
            #Del
            s = raw_input('Ho ten hoc sinh can xoa: ')
            if s in d:
                print 'Ho va ten: '+s
                print 'Ngay sinh: '+d[s][0]
                print 'Ngay sinh: '+d[s][1]
                print 'Que quan: '+d[s][2]
                del d[s]
            else:
                print 'Khong tim thay, hay thu lai.'
        elif answer == '5':
            running = False
            print 'Quit!'
        
except:
        print 'Error occurred!'
finally:
        print 'Done!'
