#n^2 + an + b > 0
#b > -(n^2 + an)
#b is prime
#b > -(40^2 + 40a)

def primelist(number):
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


	#print(prime)
	return prime

P = primelist(2000)
max_chain = -1
max_a = -1
max_b = -1
for a in range(-1000,1001):
    for b in range(1,1001):
        if(b in P):
            if(b > -1600 - 40*a and b>max_chain):
                c = 0
                n = 0
                while n*n + a*n + b in P:
                    n+=1
                    c+=1
                if c > max_chain:
                    max_a,max_b,max_chain=a,b,c
ans = max_a * max_b;
print(max_a, max_b, max_chain, ans)
