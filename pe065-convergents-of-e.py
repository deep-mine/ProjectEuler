import math

def sumOfDigits(num):
	sum = 0
	for d in str(num):
		sum += int(d)
	return sum

interger = 2
convergent = []
convergent.append(1)
convergent.append(2)
i = 0
k = 1
while len(convergent) <= 100:
	i += 1
	if i%3 != 0:
		convergent.append(1)
	else:
		k += 1
		convergent.append(2*k)

n0 = 1
n1 = 2
for i in range(99):
	c = convergent[i]
	n = c*n1 + n0
	n0 = n1
	n1 = n
	
ans = sumOfDigits(n1)
print(ans)
		


		
