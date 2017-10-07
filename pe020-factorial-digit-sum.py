#pe020
import math

number = math.factorial(100)
sum = 0
digits = str(number)
for digit in digits:
	sum += int(digit)
print(sum)