#x^2 = 1+ D*y^2
#x = sqrt(1+D*y^2)
import math

def isSquare(num):
    return math.sqrt(num) == int(math.sqrt(num))
max_x = -1
for d in range(1,20):
    if not isSquare(d):
        x = -1
        y = 1
        while x == -1:
            if isSquare(1 + d*(y**2)):
                x = math.sqrt(1 + d*(y**2))
                print(x,d,y)
                if x > max_x:
                    max_x = x;
            y += 1
print(max_x)
