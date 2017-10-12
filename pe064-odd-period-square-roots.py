import math,mathtools


def isSquare(num):
	return math.sqrt(num)==int(math.sqrt(num))
	
counter = 0

for i in range(2,10001):
	if not isSquare(i):
		if len(mathtools.continued_fraction_expansion(i))%2==1:
			counter += 1
print(counter)

		
