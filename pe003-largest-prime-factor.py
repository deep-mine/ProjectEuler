#pe003
num = 600851475143
r = 2
lim = num
while num>1 and num<=lim: 
	if num%r == 0:
		num = num / r
	else:	
		r += 1
print(r)