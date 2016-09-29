import sys
x = raw_input("input a number: ")
c = len(x)
print "the number has %d digits" % c
a = [i for i in  x]
a.reverse()
for i in range(len(x)):
    sys.stdout.write(a[i])
