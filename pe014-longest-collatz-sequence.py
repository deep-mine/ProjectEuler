#pe014

cache = {1: 1}
end = 10**6
for i in range(2,end+1):
	num = i
	counter = 0
	while num not in cache:
		if num % 2 == 0:
			num //= 2
			counter += 1
		else :
			num = ((num*3) + 1)//2
			counter += 2
	cache[i] = cache[num] + counter
print(sorted(cache.items(), key = lambda x: x[1], reverse = True)[0])

