import math
inf = 99**100


def angle(x,y):
	ans = 0
	if x == 0:
		ans =  90
	else:
		ans =  math.atan(y/x)*180/math.pi
	if y >= 0 and x>=0:
		return ans
	if y >= 0 and x < 0:
		return 180 + ans
	if y <= 0 and x<=0:
		return 180 + ans
	if y <= 0 and x > 0:
		return 360 + ans

#returns slope(m) and y-intercept(c) of line through the points
def EquationFromPoints(p1,p2):
	x1,y1,x2,y2 = list(p1)+list(p2)
	if x1!=x2:
		m = (y1-y2)/(x1-x2)
		c = (x1*y2-y1*x2)/(x1-x2)
	else:
		m = inf
		c = inf
	return (m,c)

#boolean returns if point lies on line given by two points or not
def PointOnLine(p0,p1,p2):
	x,y,x1,y1,x2,y2 = list(p0)+list(p1)+list(p2)
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
def DistanceOfPointFromLine(p0,p1,p2):
	x,y,x1,y1,x2,y2 = list(p0)+list(p1)+list(p2)
	if x1 != x2:
		c = y1 - x1*(y1-y2)/(x1-x2) #(x1*y2-x2*y1)/(x1-x2)
		m = (y1-y2)/(x1-x2)
		d = abs(c/math.sqrt(1+m*m))
	else:
		d = abs(x-x1)
	return d
	
#boolean returns true if 2 points are on the same side of a line y = mx + c
def TwoPointsSide(p1,p2,m,c):
	x1,y1,x2,y2 = list(p1)+list(p2)
	val1 = y1 - m*x1 - c
	val2 = y2 - m*x2 - c
	if val1<0 and val2<0 or val1>0 and val2>0 or val1==val2:
		return True
	else:
		return False

#tuple of points		
def TriangleArea(p1,p2,p3):
	x1,y1,x2,y2,x3,y3 = list(p1)+list(p2)+list(p3)
	return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

# list of tuple of x,y-coordinates received 
def PolygonArea(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area
	
