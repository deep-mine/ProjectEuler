b0 = 15
n0 = 21

limit = 10**12

while True:
	b = 3*b0 + 2*n0 - 2
	n = 4*b0 + 3*n0 - 3
	b0 = b
	n0 = n
	if n > limit:
		break
print(b)