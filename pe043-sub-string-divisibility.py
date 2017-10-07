
'''paper-pen'''
'''
             
d1 d2 d3 d4 d5 d6 d7 d8 d9 d10

d2 d3 d4 / 2
d3 d4 d5 / 3
d4 d5 d6 / 5
d5 d6 d7 / 7
d6 d7 d8 / 11
d7 d8 d9 / 13
d8 d9 d10 / 17

'''
for i in range (500,600):
    if i % 11 == 0:
        print(i , end = " ")
print()

'''
d6 = 0,5 -> 5
d6 d7 d8 / 11
'''

for i in range(90):
    print(i*13, end = " ")
print()

for i in range(90):
    print(i*17, end = " ")
print()

for i in range(145):
    num = i*7
    if len(str(num))==3 and str(num)[1]=="5":
        print(num, end = " ")
print()

# for i in range(20,200):
    # num = i*5
    # if len(str(num))==3 and str(num)[1]=="3" or str(num)[1]=="9":
        # if str(num)[0]!="5" and str(num)[2]=="5" and str(num)[0]!=str(num)[1]:
            # print(num, end = " ")
			
'''
d1 d2 d3 =       410,140    140,410,146,416
d3 d4 d5 =        039,        603,063
d4 d5 d6 =    195,395,495   035,135,435,635
d5 d6 d7 =     651 952     756 357 658 259
d6 d7 d8 = 506 517 528 539 561 572 583 594
d7 d8 d9 = 065     286 390     728 832
d8 d9 d10=         867 901     289

4103952867
1403952867
4106357289
4160357289
1406357289
1460357289
'''
print()
ans = 4103952867+1403952867+4106357289+4160357289+1406357289+1460357289
print(ans)