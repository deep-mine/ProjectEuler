#pe012
import math

def num_divs(n):
	nos = 0
	for i in range(1,int(round(math.sqrt(n),0))+1):
		if n%i == 0:
			nos += 2
		if i*i == n:
			nos -= 1
	return nos
	
ndivs = 0
i = 0
a = 0

while ndivs<500:
	a += i
	idx = i
	i += 1
	ndivs = num_divs(a)
	#print(a)
	#print(ndivs)
print(a)