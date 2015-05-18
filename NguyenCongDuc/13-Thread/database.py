from configloader import class_config
import redis

dbconfig = class_config('db.cfg')

class RedisModel:
    pool = ''
    def __init__(self):
        try:
            RedisModel.pool = redis.ConnectionPool(
                host = dbconfig.dict['database'],
                port = dbconfig.dict['port'],
                db = dbconfig.dict['db'])
                
            self.s = redis.Redis(connection_pool=RedisModel.pool)
            print "Connect to database successful!!"
    
        except Exception, e:
            print e
    
    def __del__(self):
        print "Closing redis"
            
    def AddMsg(self, key, value):
        try:
            self.s.lpush(key, value)
        except Exception, e:
            print "Add error", e
            
    def GetMsg(self, key):
        try:
            msg = self.s.rpop(key)
            return msg 
        except Exception,e:
            print "Get error", e
            
#duc = RedisModel()
#duc.AddMsg('z', 'NDMD')
#print duc.GetMsg('z')
