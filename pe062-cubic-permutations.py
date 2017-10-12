def digitList(num):
    dl = []
    for i in str(num):
        dl.append(int(i));
    dl.sort()
    return dl

limit = 10000
ans = 0
for i in range(5000,limit):
    count = 0
    j = i+1

    while len(digitList(i**3)) == len(digitList(j**3)):
        if digitList(i**3) == digitList(j**3):
            count += 1
        j += 1
    if count == 4:
        ans = i
        break
    print(i,count)

print(ans,ans**3)


