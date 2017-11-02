import math

x0 = 0
y0 = 10.1
x1 = 1.4
y1 = -9.6

#4x^2 + y^2 = 100

reflections = 0

while x1>0.01 or x1<-0.01 or y1<0: 
	m = -4*x1/y1
	tan2A1 = (2*m)/(1-m*m)
	
	tanA0 = (y1-y0)/(x1-x0)					   # slope of incident ray
	
	tanA2 = (tan2A1 - tanA0)/(1+tan2A1*tanA0)  # slope of reflected ray
	
	c = y1-tanA2*x1								#intercept

	x2 = (x1*(tanA2*tanA2-4)-2*tanA2*y1)/(tanA2*tanA2+4)
	y2 = tanA2*x2 + c
	
	x0,y0 = x1,y1
	x1,y1 = x2,y2
	reflections += 1
	print(x0,y0,x1,y1)
	
print(reflections)