import sys
try:
	ma=raw_input('Hay nhap ma sticker: ')
	while ma!='q':
		if ma=='1x':
			print ':)'
		elif ma=='2x':
			print ':D'
		elif ma=='3x':
			print '=))'
		else:
			print 'chuong trinh chi hieu cac ma: \'1x\', \'2x\', \'3x\''
		ma=raw_input('Hay nhap ma sticker: ', )
	print 'Ban vua nhap phim \'q\' de ket thuc chuong trinh'
except:
	print 'Ko hieu chuoi ki tu ban nhap'