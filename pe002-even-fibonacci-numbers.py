#pe002
fib = []
fib.append(1)
fib.append(2)
i = 1
while fib[i]<4000000:
	f3 = fib[i] + fib[i-1]
	fib.append(f3)
	i += 1
print(fib)
ans = sum([x for x in fib if x%2 == 0])
