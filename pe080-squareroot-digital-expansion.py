import math,mathtools

def isSquare(num):
	return math.sqrt(num) == int(math.sqrt(num))

def digitSum(root):
	dec = [int(x) for x in root if x.isdigit()][:100]
	return sum(dec)
	

summ = 0
for i in range(2,101):
	if not isSquare(i):
		root = mathtools.japanese_square_root(i,100)
		summ += digitSum(root)
print(summ)
		
		
	
	