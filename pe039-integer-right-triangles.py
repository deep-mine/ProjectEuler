#pe039
max  = -1
for p in range(7,1001):
	sols = 0
	for a in range(p//3,0,-1):
		b = (p*p - 2*a*p)//(2*p - 2*a)
		c = p-a-b
		if c*c == (a*a + b*b) and a<b and a<c and b<c:
			sols += 1
			#print(a,b,c)
	#print(p,sols)
	if sols>max:
		max = sols
		max_at = p
print(max_at)