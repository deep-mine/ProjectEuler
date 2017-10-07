import math

def gcd(a,b):
    while a != 0:
        a , b = b%a, a
    return b


def inverseModulus(a,m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3),v1, v2, v3
    return u1 % m

def combination(a,b):
	c = min(b,a-b)
	p = 1
	for i in range(c):
		p *= (a-i)
	return p/(math.factorial(c))
	
def permutation(a,b):
	c = min(b,a-b)
	p = 1
	for i in range(c):
		p *= (a-i)
	return p
	
def divisorlist(num):
	div = []
	for i in range(1,int(math.sqrt(num))+1):
		if num%i==0:
			div.append(i)
			if num//i not in div:
				div.append(num//i)
	return (sorted(div))
	
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
	return prime

a = [int(x) for x in input().split(" ")].sort()
print(a)