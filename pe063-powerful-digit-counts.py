#pe063
counter = 0
for i in range(1,10):
	for j in range(23):
		if len(str(i**j)) == j:
			counter += 1
			print(i**j,j)
print(counter)
