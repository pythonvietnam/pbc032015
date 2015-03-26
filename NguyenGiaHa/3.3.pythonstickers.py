try:
	x=raw_input('Hay nhap ma sticker muon hien: ')
	while x!='q':
		if x=='1x':
			print ':)'
			break
		elif x=='2x':
			print ':))'
			break
		elif x=='3x':
			print ':)))'
			break
		else:
			x=raw_input('Hay nhap dung ma sticker muon hien: ')
	else:
		print 'Ban vua nhap phim Q, chuong trinh se ket thuc!'
except:
	print 'Da co loi xay ra!'
finally:
	print 'Done!'
