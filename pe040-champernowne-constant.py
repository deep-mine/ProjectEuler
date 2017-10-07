#pe040
d = '.'+''.join(str(i) for i in range(1,1000000))
p = 1
for i in range(7):
	p *= int(d[10**i])
print(p)