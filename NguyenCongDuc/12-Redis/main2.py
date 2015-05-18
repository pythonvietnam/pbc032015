# Ham day du lieu vao redis

from database import RedisModel
from sys import argv

if __name__ == '__main__':
    b = RedisModel()
    b.GetMsg('z')
    