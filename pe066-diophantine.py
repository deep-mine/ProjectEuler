#x^2 = 1+ D*y^2
import math,mathtools

def isSquare(num):
	return math.sqrt(num) == int(math.sqrt(num))
max_h = -1
for d in range(2,1001):
	if not isSquare(d):
		cfr = mathtools.continued_fraction_representation(d)
		h_2,h_1 = 0,1
		k_2,k_1 = 1,0
		i = 0
		while True:
			h = cfr[i]*h_1 + h_2
			k = cfr[i]*k_1 + k_2
			if h*h-d*k*k -1 == 0:
				break
			h_2,k_2,h_1,k_1 = h_1,k_1,h,k
			i += 1
			if i==len(cfr):
				i = 1
		if h > max_h:
			max_h = h
			ans = d
		print(max_h,ans)