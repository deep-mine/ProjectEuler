import math

lim = 10**6
cache = {1454:3,169:3,363601:3,871:2,45361:2,872:2,45362:2}

def factorial_sum(num):
	sum = 0
	for d in str(num):
		sum += math.factorial(int(d))
	return sum

for i in range(lim+1):
	if i in cache:
		continue
	else:
		prev = []
		prev.append(i)
		cache[i] = 1
		num = factorial_sum(i)
		while num not in cache:
			prev.append(num)
			cache[num] = 0
			for p in prev:
				cache[p] += 1
			num = factorial_sum(num)
		if num in cache:
			if num != factorial_sum(num):
				for p in prev:
					cache[p] += cache[num]
			else:
				for p in prev:
					cache[p] += 1
				

		
ans = 0
for item in cache:
	if cache[item] == 60:
		ans += 1
print(ans)
