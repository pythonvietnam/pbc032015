#!/usr/bin/python
# coding: utf-8
# ducnc92@hotmail.com
# Chuong trinh doc file config

#from sys import argv

def config_parse(conf_file):

    D = {}
    handle = open(conf_file,'r')
    for line in handle:
        line = line.strip()
        if line.startswith('#') or line == '':
            pass
        else:
            line = line.split('=')
            a = line[0].strip()
            b = line[1].strip()
            D[a] = b
    return D

def main(conf_file = 'D:\Python\pbc032015\NguyenCongDuc\config.cfg'):
    
    D = config_parse(conf_file)
    
    for key in config_parse(conf_file):
        if key == 'database':
            print "Database name is: ", D[key]
        elif key == 'user':
            print "User name is: ", D[key]
        elif key == 'password':
            print "Password is: ", D[key]
            
if __name__ == '__main__':
    main()