#pe028
NE = []
SW = []
NW_SE = []
n = 1001
for i in range(1,n+1,2):
	NE.append(i**2)
for i in range(2,n,2):
	SW.append(i**2+1)
val = 1
for i in range(1,n):
	NW_SE.append(val+2*i)
	val = val+2*i
sum = sum(NE)+sum(SW)+sum(NW_SE)
#print(NE)
#print(SW)
#print(NW_SE)
print(sum)