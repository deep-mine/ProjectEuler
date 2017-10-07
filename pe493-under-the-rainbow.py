import math

def combination(a,b):
	return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
	

ans = combination(60,20)/combination(70,20)

print(7*(1-ans))