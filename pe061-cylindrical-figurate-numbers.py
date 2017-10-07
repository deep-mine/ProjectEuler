import math

def isTriangle(num):
    n = (math.sqrt(8*num+1)-1)/2
    return n == int(n)

def isSquare(num):
    return math.sqrt(num)==int(math.sqrt(num))

def isPentagonal(num):
    n = (math.sqrt(24*num+1)+1)/6
    return n == int(n)

def isHexagonal(num):
    n = (math.sqrt(8*num+1)+1)/4
    return n == int(n)

def isHeptagonal(num):
    n = (math.sqrt(40*num+9)+3)/10
    return n == int(n)

def isOctagonal(num):
    n = (math.sqrt(3*num+1)+1)/3
    return n == int(n)

def digList(num):
    l = []
    for i in str(num):
        l.append(int(i))
    return l

tlist = []
for i in range(1000,10000):
    if isTriangle(i) and "0" not in str(i) and len(digList(i)) == len(set(digList(i))):
        tlist.append(i)

slist = []
for i in range(1000,10000):
    if isSquare(i) and "0" not in str(i) and len(digList(i)) == len(set(digList(i))):
        slist.append(i)

plist = []
for i in range(1000,10000):
    if isPentagonal(i) and "0" not in str(i) and len(digList(i)) == len(set(digList(i))):
        plist.append(i)

hexlist = []
for i in range(1000,10000):
    if isHexagonal(i) and "0" not in str(i) and len(digList(i)) == len(set(digList(i))):
        hexlist.append(i)

heplist = []
for i in range(1000,10000):
    if isHeptagonal(i) and "0" not in str(i) and len(digList(i)) == len(set(digList(i))):
        heplist.append(i)

olist = []
for i in range(1000,10000):
    if isOctagonal(i) and "0" not in str(i) and len(digList(i)) == len(set(digList(i))):
        olist.append(i)

print(tlist)
print(slist)
print(plist)
print(hexlist)
print(heplist)
print(olist)
