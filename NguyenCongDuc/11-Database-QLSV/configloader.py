#!/usr/bin/python
# coding: utf-8
# ducnc92@hotmail.com
# Class dung de doc file config

import sys

class class_config:
    
    #doc string
    '''Class dung de doc file config co san'''
    
    def __init__(self, conf_file):
    #Ham dung de mo file config
        try:
            self.f = open(conf_file)
            self.config_parse()
        except Exception, e:
            print "Co loi khi mo file config"
            print e
            exit()
        
    def __del__(self):
    #Ham dung de dong file config
        try:
            self.f.close()
            self.f.close()
        except Exception, e:
            print "Error when close file config", e
            
    def config_parse(self):
    #Ham dung de tach chuoi lay thong tin cua file config
        self.dict = {}
        for line in self.f:
            line = line.strip()
            if line.startswith('#') or line == '':
                pass
            else:
                line = line.split('=')
                a = line[0].strip()
                b = line[1].strip()
                self.dict[a] = b
                
        return dict
        
#Test config
if __name__ == '__main__':
    a = class_config('db.cfg')
    print a.dict
    