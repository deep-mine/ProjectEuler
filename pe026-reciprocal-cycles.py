#pe026
max = 0 
for i in range(2,1001):
	decimal = []
	remainder = []
	number = 10**(len(str(i)))
	for j in range(len(str(number))-2):
		decimal.append(0)
	r = -1
	while r not in remainder[:-1] :
		d = number//i
		r = number%i
		decimal.append(d)
		remainder.append(r)
		number = r*10
	idx = remainder.index(r)
	#print(i,end = " 0.")
	#print(*decimal)
	if len(decimal)>max:
		max = i
print(max)
	
		
	
