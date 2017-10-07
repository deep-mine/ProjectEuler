#p041
import primecache


def isPan(a):
    pan = []
    for i in range(len(str(a))):
        pan.append(i+1)
    count = 0
    for digs in pan:
        if str(digs) in str(a):
            count += 1
    return count==len(str(a))

primes = primecache.primelist(10**7)
for i in primes[::-1]:
    if isPan(i):
        print(i)
        break
