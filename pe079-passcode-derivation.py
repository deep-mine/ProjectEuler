with open("C:\\Users\\Dibyanshu\\Desktop\\Project Euler\\p079_keylog.txt") as n:
	numbers = n.read().split("\n")
	
numbers = list(set(numbers[:-1]))
code = ''
numbefore = {}
numafter  = {}
for i in range(10):
	numbefore[i] = []
	numafter[i]  = []

for i in range(10):
	for num in numbers:
		if str(i) in str(num):
			idx = 0
			while str(num)[idx]!=str(i):
				if str(num)[idx] not in numbefore[i]:
					numbefore[i] += [str(num)[idx]]
				idx += 1
			idafter = str(num).index(str(i))
			while idafter < 3:
				if str(num)[idafter] not in numafter[i]:
					numafter[i] += [str(num)[idafter]]
				idafter += 1
				

for i in range(10):
	numbefore[i] = len(numbefore[i])
	numafter[i]  = len(numafter[i])

possible_digits = {}

for i in range(10):
	if numbefore[i]>0 or numafter[i]>0:
		possible_digits[i] = numbefore[i]
		
c = sorted([(k,v) for (v,k) in possible_digits.items()])

for i in range(len(c)):
	code += str(c[i][1])
print(code)


				


