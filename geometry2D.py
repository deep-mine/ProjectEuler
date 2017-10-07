import math
inf = 99**100

#returns slope(m) and y-intercept(c) of line through the points
def EquationFromPoints(x1,y1,x2,y2):
	if x1!=x2:
		m = (y1-y2)/(x1-x2)
		c = (x1*y2-y1*x2)/(x1-x2)
	else:
		m = inf
		c = inf
	return (m,c)

#boolean returns if point lies on line given by two points or not
def PointOnLine(x,y,x1,y1,x2,y2):
	if x1 != x2:
		val = (y-y1) - (y1-y2)/(x1-x2)*(x-x1)
	else:
		val = x-x1
	if val == 0:
		return True
	else:
		return False

#float returns distance of a point from a line given by two points
# d = c/sqrt(m^2+1)
def DistanceOfPointFromLine(x,y,x1,y1,x2,y2):
	if x1 != x2:
		c = y1 - x1*(y1-y2)/(x1-x2) #(x1*y2-x2*y1)/(x1-x2)
		m = (y1-y2)/(x1-x2)
		d = abs(c/math.sqrt(1+m*m))
	else:
		d = abs(x-x1)
	return d
	
#boolean returns true if 2 points are on the same side of a line y = mx + c
def TwoPointsSide(x1,y1,x2,y2,m,c):
	val1 = y1 - m*x1 - c
	val2 = y2 - m*x2 - c
	if val1<0 and val2<0 or val1>0 and val2>0 or val1==val2:
		return True
	else:
		return False
		

n,k = [int(x) for x in input().split(" ")]
print(n,k)