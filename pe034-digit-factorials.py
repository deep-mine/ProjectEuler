#pe034
import math
ans = 0
for i in range(3,99999):
	sum = 0
	for j in str(i):
		sum += math.factorial(int(j))
	if sum == i:
		ans += i
print(ans)