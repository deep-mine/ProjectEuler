import math

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

with open('C:\\Users\\Dibyanshu\\Desktop\\Project Euler\\p102_triangles.txt') as t:
	points = t.read().split('\n')
points = points[:-1]

triangles = []

for coords in points:
	triangles.append(coords.split(','))

has_zero = 0
origin = 0
	
for i in range(len(triangles)):
		x1 = int(triangles[i][0])
		y1 = int(triangles[i][1])
		
		x2 = int(triangles[i][2])
		y2 = int(triangles[i][3])
		
		x3 = int(triangles[i][4])
		y3 = int(triangles[i][5])
		
		if (x1==0 and y1==0) or (x2==0 and y2==0) or (x3==0 and y3==0):
			has_zero += 1
			origin += 1
			
		else:
			angle1 = angle(x1,y1)
			angle2 = angle(x2,y2)
			angle3 = angle(x3,y3)
			angles = [angle1,angle2,angle3]
			angles.sort()
			
			if angles[2]-angles[0]>180 and angles[1]-angles[0]<180 and angles[2]-angles[1]<180:
				has_zero += 1

print(has_zero)
		