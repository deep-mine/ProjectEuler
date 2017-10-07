import primecache

p = primecache.primelist(10**5)

def countPrime(nlist):
    count = 0
    for i in nlist:
        if i in p:
            count+=1
    return count

rounds = 1
numlist = []
numlist.append(1)

while True:
    for i in range(1,5):
        numlist.append(numlist[-1]+2*rounds)
    rounds += 1
    #print((rounds-1),(rounds-1)*2+1,numlist,countPrime(numlist),len(numlist),countPrime(numlist)/len(numlist))
    if countPrime(numlist)/len(numlist) < 0.1:
        break
print((rounds-1)*2+1)
