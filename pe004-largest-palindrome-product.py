#pe004
def palindrome(check):
	sc = str(check)
	tr = ""
	for i in sc[::-1]:
		tr += i
	if(sc==tr):
		return True
	else:
		return False
		
ans = 0		
for i in range(999,100,-1):
	for j in range(999,100,-1):
		ans_p = i*j
		if palindrome(ans_p) and ans_p >= ans:
			ans = ans_p
			print(ans)

			