# -*- coding: utf-8 -*-
import sys
import codecs
print ('Chao mung ban!')
tuoi=18
tuoinhap=int(raw_input(' Vui long cho chung toi biet so tuoi cua ban '))
if tuoinhap >= tuoi:
	print('ban da du tuoi')
elif tuoinhap < tuoi:
	print ('Ban chua du tuoi')
else:
	print "sai roi"
