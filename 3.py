import math
no_number = True
for i in range(1000000):
    x = int (math.sqrt(i+100))
    y = int (math.sqrt(i+268))
    if(x*x == i+100) and (y*y == i+268):
        print i
        no_number = False
if(no_number):
    print"no such number"
