#pe024
import itertools

permute = itertools.permutations('0123456789',10)
perm = []
for i in permute:
	perm.append(i)
ans = ''
for value in perm[999999]:
	ans += value
print(ans)
