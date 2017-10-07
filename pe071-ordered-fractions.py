a = 3
b = 7
r = 0
s = 1
l = 1000000

for q in range(3,l,2):
    p = ((a*q-1)//b)
    if p*s>q*r:
        r = p
        s = q
print(r,s)
