#pe021
import math
def divisor_list(num):
	div = []
	for i in range(1,int(math.sqrt(num))+1):
		if num%i==0:
			div.append(i)
			if num//i not in div:
				div.append(num//i)
	return (sorted(div))

amicable = []
for i in range(1,10001):
	x = sum(divisor_list(i)[:-1])
	y = sum(divisor_list(x)[:-1])
	if i==y and x!=y:
		amicable.append(i)
		if y not in amicable:
			amicable.append(y)

print(sum(amicable))