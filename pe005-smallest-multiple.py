#pe05
def lcm(a1,b1):
	a = max(a1,b1)
	b = min(a1,b1)
	(m,n) = (a,b)
	while b != 0:
		(a,b) = (b,a%b)
	return m*n//a

ans = 1
for i in range(2,21):
	ans = lcm(i,ans)
print(ans) 
