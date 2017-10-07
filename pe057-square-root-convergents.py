n = []
d = []
n.append(3)
d.append(2)
count = 0
for i in range(1000):
    d.append(n[-1]+d[-1])
    n.append(n[-1]+2*d[-2])
    if len(str(n[-1])) > len(str(d[-1])):
        count+=1
print(count)
