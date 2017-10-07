def match(num):
    s = str(num)
    return not all(int(s[i*2]) == i+1 for i in range(9))

n = 138902663
while match(n*n):
    n -= 2

print(n*10)
