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
	
def doDecimal(num,digs):
	n = num
	n = math.floor(n*10**digs)
	n = n/10**digs
	return n

def babylonian_square_root(num,acc):
	x0 = 10
	x_revised = 0
	x_prev = -1
	iter = 0
	while iter < 10:
		x_prev = x_revised
		x_revised = (x0 + num/x0)/2
		x0 = x_revised
		iter += 1
		print(x0)
	return x0
	
def continued_fraction_expansion(num):
	a0 = math.floor(math.sqrt(num))
	m,d,a = [0,1,a0]
	cache = []
	#cache.append((m0,d0,a0))
	while a != 2*a0:				#https://studylib.net/doc/7921613/on-continued-fractions-of-the-square-root-of-prime-numbers
		m = d*a-m
		d = (num - m*m)/d
		a = math.floor((a0 + m)/d)
		cache.append((m,d,a))
	return cache

def continued_fraction_representation(num):
	a0 = math.floor(math.sqrt(num))
	m,d,a = [0,1,a0]
	cache = []
	cache.append(a0)
	while a != 2*a0:
		m = d*a-m
		d = (num - m*m)/d
		a = math.floor((a0 + m)/d)
		cache.append(a)
	return cache
	
#takes in list of convergents from continued_fraction_representation
def continuants(convergents):
	h = []
	k = []
	h.append(convergents[0]*1 + 0)
	h.append(convergents[1]*h[0] + 1)
	k.append(convergents[0]*0 + 1)
	k.append(convergents[1]*k[0] + 0)
	
	for i in range(2,len(convergents)):
		h.append(convergents[i]*h[i-1] + h[i-2])
		k.append(convergents[i]*k[i-1] + k[i-2])
	return (h,k)
	
	
#returns square root as a string of length (size)
def japanese_square_root(num,size):
	a = 5*num
	b = 5
	
	while len(str(b))<=200:
		if a >= b:
			a = a-b
			b += 10
		else:
			a *= 100
			b = int(str(b)[:-1]+'0'+str(b)[-1])
			
	decimal_pos = len(str(math.floor(math.sqrt(num))))
	b = str(b)[:decimal_pos]+'.'+str(b)[decimal_pos:][:size]
	return b
