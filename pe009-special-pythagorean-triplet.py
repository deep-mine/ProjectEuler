#pe09

n = 1000
ans = 0
for a in range(n//3,0,-1):
	b = (2*n*a - n**2)//(2*(a-n))
	c = n-a-b
	if c**2 == a**2 + b**2  and c>a and c>b and b>a:
		ans = a*b*c
		print(a,b,c,ans)
print(ans)