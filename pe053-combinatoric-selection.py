#pe053
import math

counter = 0

for i in range(101):
	for j in range(i+1):
		c = math.factorial(i)//(math.factorial(j)*math.factorial(i-j))
		if c>1000000:
			counter += 1
print(counter)
