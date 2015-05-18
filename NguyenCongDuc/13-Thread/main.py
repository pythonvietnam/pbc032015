# Ham day du lieu vao redis

from database import RedisModel
from sys import argv
import threading
import time

if __name__ == '__main__':

    def addmsg(key, msg):
        a = RedisModel()
        a.AddMsg(key, msg)
        print "Adding message!"

    def getmsg(key):
        time.sleep(10)
        b = RedisModel()
        msg =  b.GetMsg(key)
        print msg
        
    t1 = threading.Thread(name="Thread 1", target=addmsg, args=('a','Nguyen Cong Duc'))
    t1.start()
    t2 = threading.Thread(name="Thread 2", target=getmsg, args=('a'))
    t2.start()