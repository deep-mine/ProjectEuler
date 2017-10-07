#pe030
def power_digit_sum(num):
	sum = 0
	power = 5
	for i in str(num):
		sum += int(i)**power
	return sum
	
pds = []		
for i in range(2,200000):
	if i == power_digit_sum(i):
		pds.append(i)
#print(pds)
print(sum(pds))
	