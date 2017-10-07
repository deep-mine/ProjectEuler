#pe035
import itertools
def all_perms(num):
	permute = itertools.permutations(str(num),len(str(num)))
	perm = []
	for i in permute:
		val = [x for x in i]
		perm.append(val)
	perm_list = []
	for p in perm:
		num = ''
		for i in p:
			num+=i
		if int(num) not in perm_list:
			perm_list.append(int(num))
	#print(perm_list)
	return perm_list

p = [True]*(1000000)
p[0] = False
p[1] = False
	
for i in range(2, len(p)):
	for j in range(i*i, len(p), i):
		if p[j]:
			p[j] = False
				
prime = []
for i in range(len(p)):
	if p[i]:
		prime.append(i)
count = 0
for i in range(1,1000001):
	if (len(all_perms(i))) == len(set(all_perms(i)) & set(prime)):
		count += 1
		print(i)
print(count)
			
	