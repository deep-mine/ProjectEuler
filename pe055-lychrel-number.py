def Palindrome(num):
    return str(num)==str(num)[::-1]

def Rev(num):
    return int(str(num)[::-1])
count = 0
# for i in range(4994,10000):
#     sum = 0
#     iter = 0
#     num = i
#     if Palindrome(num):
#         print(num)
#         while iter<50:
#             sum = num + Rev(num)
#             print(sum)
#             iter += 1
#             if Palindrome(sum):
#                 break
#     if iter==50:
#         count += 1
# print(count)

for i in range(10000):
    sum = 0
    iter = 0
    num = i
    while iter<50:
        sum = num + Rev(num)
        num = sum
        iter += 1
        if Palindrome(sum):
            break
    if iter==50:
        count += 1
        #print(num,count)

print(count)
