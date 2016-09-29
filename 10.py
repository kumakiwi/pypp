import time
print time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time()))
time.sleep(1)
print time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time()))
