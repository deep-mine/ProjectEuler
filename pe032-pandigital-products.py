def checkPan(a,b,m):
    digs = []
    count = 0
    for i in str(a):
        digs.append(int(i))
    for i in str(b):
        digs.append(int(i))
    for i in str(m):
        digs.append(int(i))
    pandig = [1,2,3,4,5,6,7,8,9]
    for i in pandig:
        if i in digs:
            count += 1
    if count == 9:
        print(a,b,m,digs)
        return True
    else:
        return False

sum = 0
count = 0
prods = []
for i in range(1,10):
    for j in range(1000,10000):
        if len(str(i*j))+len(str(i))+len(str(j))==9 and (i*j) not in prods:
            if checkPan(i,j,i*j):
                sum += i*j
                count +=1
                prods.append(i*j)
for i in range(10,100):
    for j in range(100,1000):
        if len(str(i*j))+len(str(i))+len(str(j))==9 and (i*j) not in prods:
            if checkPan(i,j,i*j):
                sum += i*j
                count +=1
                prods.append(i*j)
print(sum,count)
print(prods)
