peter = [[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4],
		[1,2,3,4]]
nick  = [[1,2,3,4,5,6],
		[1,2,3,4,5,6],
		[1,2,3,4,5,6],
		[1,2,3,4,5,6],
		[1,2,3,4,5,6],
		[1,2,3,4,5,6]]

sum_peter = {}
sum_nick  = {}

for i in range(6,37):
	sum_peter[i] = 0
	sum_nick[i]  = 0

for a in range (4):
	for b in range(4):
		for c in range(4):
			for d in range(4):
				for e in range(4):
					for f in range(4):
						for g in range(4):
							for h in range(4):
								for i in range(4):
									sum = peter[0][a]+peter[1][b]+peter[2][c]+peter[3][d]+peter[4][e]+peter[5][f]+peter[6][g]+peter[7][h]+peter[8][i]
									sum_peter[sum] += 1

				
for a in range (6):
	for b in range(6):
		for c in range(6):
			for d in range(6):
				for e in range(6):
					for f in range(6):
						sum = nick[0][a]+nick[1][b]+nick[2][c]+nick[3][d]+nick[4][e]+nick[5][f]
						sum_nick[sum] += 1

pwins = 0

for n in range(6,36):
	for p in range(n+1,37):
		pwins += sum_nick[n]*sum_peter[p]

print(pwins/(4**9*6**6))

