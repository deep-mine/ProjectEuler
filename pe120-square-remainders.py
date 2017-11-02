summ = 0
for a in range(3,1001):
	if a%2==0:
		r=a*(a-2)
	else:
		r = a*(a-1)
	summ += r
print(summ)