#pe036
def dtob(num):
	dec = []
	d = num
	'''
	while d!=0:
		r = d%2
		d //=2
		dec.append(r)
	for i in dec[::-1]:
		ans+=str(i)
	return int(ans)
	'''
	return bin(d)[2:]
	
sum = 0
for i in range(1,1000000):
	bin_ = dtob(i)
	if str(i)==str(i)[::-1] and str(bin_)==str(bin_)[::-1]:
		sum+=i
print(sum)