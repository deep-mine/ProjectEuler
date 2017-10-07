#pe045
from math import sqrt
hex = []
for i in range(1,100000):
	hex.append((2*i-1)*i)
for num in hex:
	if (sqrt(1+24*num)+1)%6 == 0 and (sqrt(1+8*num)+1)%2==0:
		print(num)