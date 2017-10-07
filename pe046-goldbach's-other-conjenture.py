#composite = prime + 2*square

import primecache
import math

def isSquare(num):
    return math.sqrt(num) == int(math.sqrt(num))

plist = primecache.primelist(10000)
clist = []
for p in range(2,10000):
    if p not in plist:
        clist.append(p)

print(plist)
print(clist)
passnum = []
for c in clist:
    check = 0
    found = False
    for p in plist:
        #check = 0
        if c>p and isSquare(int((c-p)/2)):
            check *= 0
            found = True
            break
        else:
            check += 1
    if found == True:
        passnum.append(c)
        print(c,p)
for c in clist:
    if c not in passnum:
        print(c)
