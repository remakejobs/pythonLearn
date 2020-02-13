import random
import os
import time
secret = random.randint(1,20)
print(secret)
print("获取当前时间")
print(time.localtime(os.path.getatime("E:\\5.product\\python\\pythonLearn\\project\\filesys.py")))
