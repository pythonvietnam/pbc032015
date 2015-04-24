from configclass import class_config
from sys import argv

def print_info(x):
    print "Database name is: ", x['database']
    print "User name is: ", x['user']
    print "User name is: ", x['password']


if __name__ == '__main__':
    if len(argv) != 2:
        print 'Hay nhap theo dinh dang "python 10callconfig.py path_to_configfile"'
        exit()
    script, file = argv
    duc = class_config(file)
    x = duc.dict
#    print duc.__doc__
    print_info(x)

    
'''
    for key in duc.dict:
        if key == 'database':
            print "Database name is: ", duc.dict[key]
        elif key == 'user':
            print "User name is: ", duc.dict[key]
        elif key == 'password':
            print "Password is: ", duc.dict[key]
'''