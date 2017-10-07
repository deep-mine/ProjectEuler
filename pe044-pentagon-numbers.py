#pentagon number
import math

'''
n(3n-1)/2
pj = j(3j-1)/2
pk = k(3k-1)/2

pj-pk = (3j^2-j-3k^2+k)/2
        (3(j+k)(j-k)-(j-k))/2
        ((j-k)(3(j+k)-1))/2

pj+pk = (3(j^2+k^2) - (j+k))/2
        (3(j+k)^2 - 2jk - (j+k))/2
        (j+k) (3(j+k)-1)/2 - jk

2p = 3n^2-n
3n^2-n-2p=0
n = (1 +/- sqrt(1+24p))/6


'''
def isPentagon(num):
    n = (1+ math.sqrt(24*num+1))/6
    return n == int(n)

notfound = True
i = 1
while (notfound):
    i += 1
    n1 = i*(3*i - 1)/2
    for j in range(i-1,0,-1):
        n2 = j*(3*j - 1)/2
        if isPentagon(n1+n2) and isPentagon(n1-n2):
            print(int(n1-n2))
            notfound = False
            break
