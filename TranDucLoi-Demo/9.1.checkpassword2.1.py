# checkpassword version 2.1
# loitd
# devide into functions
# read pw from file

import zipfile
import sys
import os

def checkzip(filename, password):
	try:
		z = zipfile.ZipFile(filename)
		z.extractall(pwd=password) #all the file extracted will be in the running folder
		print "yahoo00. this is the password."
		return password
	except Exception, e:
		print e #because I am lazy :D
		return False

def readpwd(filename, keyfilename):
	try:
		keys = open(keyfilename, 'r')
		for key in keys.readlines():
			key = key.strip('\n')
			print "Testing with password: " + key
			chkresult = checkzip(filename, key)
			if chkresult != False:
				print "Password found: " + chkresult
				exit(0)
			else:
				print "No Password found!"
		return
	except Exception, e:
		print e
		return False

def main():
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		keyfilename = sys.argv[2]
		if os.path.isfile(filename) and os.path.isfile(keyfilename):
			if os.access(filename, os.R_OK) and os.access(keyfilename, os.R_OK):
				#checkzip(filename, "123456")
				readpwd(filename, keyfilename)
			else:
				print 'Error: ' + filename + ' can not be read.'
				exit(0)
		else:
			print 'Error: ' + filename + ' does not exist.'
			exit(0)
	else:
		print "Enter enough params:\n"
		print "Usage: checkpassword2.1 filename keyfilename"

if __name__ == '__main__':
	main()