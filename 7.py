def addlist(l):
    for n in range(5):
        tmp = int(raw_input( "%s number of list: "% str(n+1)))
        l.append(tmp)
    return l
l = []
addlist(l)
b = l[:]
print b:"\n"

