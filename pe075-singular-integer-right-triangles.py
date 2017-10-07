import mathtools,math

lim = 15*10**5
triples = []
for s in range(3,math.floor(math.sqrt(lim)),2):
	for t in range(s-2,0,-2):
		if math.gcd(s,t)==1:
			a = s*t
			b = (s*s-t*t)//2
			c = (s*s+t*t)//2
			triples.append([a,b,c])

vals = [0]*(lim+1)

for triple in triples:
	summ = sum(triple)
	for i in range(summ,len(vals),summ):
		vals[i] += 1
		
ans = 0
for i in vals:
	if i==1:
		ans += 1
		
print(ans)
		
		
		




















































# def popitem(r,val):
	# id = -1
	# for i in range(len(r)):
		# if val == r[i]:
			# id =  i
			# break
	# r.pop(id)
	# return r

# fib = []
# fib.append(1)
# fib.append(1)
# for i in range(2,100):
	# if len(str(fib[-1])) < 8:
		# fib.append(fib[i-1]+fib[i-2])
# right_triangles = {5:[5,4,3,12]}
# for i in range(6,len(fib),2):
	# right_triangles[fib[i]] = [fib[i],fib[i-2]+right_triangles[fib[i-2]][2]+right_triangles[fib[i-2]][1],fib[i-1]-right_triangles[fib[i-2]][2]]
	# right_triangles[fib[i]].append(right_triangles[fib[i]][0]+right_triangles[fib[i]][1]+right_triangles[fib[i]][2])

# pprint.pprint(right_triangles)

# print(mathtools.divisorlist(610))




# r = [1,2,3,4,5,3]

# r = popitem(r,2)
# print(r)


