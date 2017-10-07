import mathtools,math

limit = 2*10**6
min = 10**10
m,n = 0,0
for i in range(100):
	for j in range(100):
		ans = i*(i+1)*j*(j+1)/4
		d = abs(ans-limit)
		if d < min:
			min = d
			m,n = i,j
print(m,n,m*n)
			

