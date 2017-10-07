#pe007
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
		if len(prime)==10001:
			break
			
	#print(prime)
	return prime[-1]
	
ans = prime_num(999999)
print(ans)

	
	