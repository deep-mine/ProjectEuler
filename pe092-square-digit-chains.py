#pe092
chain1 = [1]
chain89 = [89]

def digSquare(num):
    s = 0
    for d in str(num):
        s += int(d)**2
    return s
print()
for i in range(1,10000000):
    temp = []
    n1  = i
    while n1!=1 and n1!=89:
        if n1 in chain89 or n1 in chain1:
            break
        if n1 not in temp:
            temp.append(n1)
        temp.append(digSquare(n1))
        n1 = temp[-1]

    if n1 == 1 or n1 in chain1:
        chain1 += temp
    else:
        chain89 += temp
    #print(i,temp)
#print(1,chain1)
#print(89,chain89)
print(sum(chain89))