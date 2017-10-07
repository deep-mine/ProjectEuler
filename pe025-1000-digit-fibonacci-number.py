#pe025
fib = []
fib.append(0)
fib.append(1)
digit = 1
i = 2
max_digit = 1000
while digit<max_digit:
	fib.append(fib[i-1] + fib[i-2])
	digit = len(str(fib[i]))
	i += 1
print(i-1,fib[-1])


