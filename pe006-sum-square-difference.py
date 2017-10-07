#pe006
n = 100
sum_of_square = n*(n+1)*(2*n+1)//6
square_of_sum = (n*(n+1)//2)**2
ans = abs(sum_of_square-square_of_sum)
print(ans)