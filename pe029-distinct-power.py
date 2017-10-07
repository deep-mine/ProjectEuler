#pe029
num_list = []
for a in range(2,101):
	for b in range(2,101):
		num = a**b
		if num not in num_list:
			num_list.append(num)
print(len(num_list))