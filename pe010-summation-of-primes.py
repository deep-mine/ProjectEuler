#pe010
def prime_num(number):
	p = [True]*(number+1)
	p[0] = False
	p[1] = False
	
	for i in range(2, len(p)):
		for j in range(i*i, len(p), i):
			if p[j]:
				p[j] = False
				
	prime = []
	for i in range(len(p)):
		if p[i]:
			prime.append(i)
	
	return sum(prime)
	
ans = prime_num(2000001)
print(ans)
