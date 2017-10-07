# 9234 9487

def isPan(a,b):
    pan = [1,2,3,4,5,6,7,8,9]
    count = 0
    if len(str(a)) + len(str(b)) == 9:
        for digs in pan:
            if str(digs) in str(a) or str(digs) in str(b):
                count += 1
    return count==9

for i in range(9487,9233,-1):
    if isPan(i,2*i):
        print(str(i)+str(2*i))
        break
