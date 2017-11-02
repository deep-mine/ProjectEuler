def checkBounce(num):
	bounce = {'UP':0,'DOWN':0}
	for i in range(len(str(num))-1):
		if int(str(num)[i])>int(str(num)[i+1]):
			bounce['DOWN']+=1
		elif int(str(num)[i])<int(str(num)[i+1]):
			bounce['UP'] +=1
	if bounce['UP'] != 0 and bounce['DOWN']!=0:
		return True
	else:
		return False
		
counter = 0
perc = 0
i = 100
limit = 99
while perc <= limit:
	if checkBounce(i):
		counter += 1
	perc = counter*100/(i)
	i += 1
	
print(i-2)

		