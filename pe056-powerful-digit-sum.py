#pe056
def digsum(num):
	sum = 0
	for d in str(num):
		sum += int(d)
	return sum

max = -1
for a in range(101):
	for b in range(101):
		num = a**b
		dsum = digsum(num)
		if dsum>max:
			max = dsum
print(max)
