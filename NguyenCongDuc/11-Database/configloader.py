#!/usr/bin/python
# coding: utf-8
# ducnc92@hotmail.com
# Class dung de doc file config

import sys

class class_config:
    
    #doc string
    '''Class dung de doc file config co san'''
    
    def __init__(self, conf_file):
        try:
            self.f = open(conf_file)
            self.config_parse()
        except Exception, e:
            print "Co loi khi mo file config"
            print e
            exit()
        
    def __del__(self):
        try:
            self.f.close()
            print "Close config file"
            self.f.close()
        except Exception, e:
            print 'error'
            
    def config_parse(self):
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
                
#Test config
if __name__ == '__main__':
    a = class_config('db.cfg')
    print a.dict
    