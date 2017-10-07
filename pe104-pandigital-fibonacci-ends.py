def panfib(num):
	f9 = str(num)[:9]
	l9 = str(num)[-9:]
	
	for i in range(1,10):
		if str(i) not in f9 or str(i) not in l9:
			return False
	return True
	
fib = []
fib.append(1)
fib.append(1)

ans = 0
i   = 0
notfound = True
while notfound:
	f = fib[i]+fib[i+1]
	fib.append(f)
	if panfib(f):
		ans = i+3
		notfound = False
	i += 1
	print(i+3)
print(ans)
		