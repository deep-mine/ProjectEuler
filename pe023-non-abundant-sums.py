#pe023
import math

def divsum(n):
	divs = []
	divs.append(1)
	for i in range(2,int(round(math.sqrt(n),0))+1):
		if n%i == 0:
			divs.append(i)
			if n//i not in divs:
				divs.append(n//i)
	return sum(divs)

end = 28123
abundant = []
for i in range(1,end+1):
	if divsum(i)>i:
		abundant.append(i)		


not_sum = [False]*(end+1)
for x in abundant:
	for y in abundant:
		if x+y<(end+1):
			not_sum[x+y] = True

sum = 0
for i,b in enumerate(not_sum):
	if not b:
		sum += i
print(sum)