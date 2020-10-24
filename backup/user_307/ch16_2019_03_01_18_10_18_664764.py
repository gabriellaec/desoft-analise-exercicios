import math
x1=2
y1=2
x2=3
y2=3

def distancia_euclidiana(x1,y1,x2,y2):
	y=math.sqrt((x1-x2)**2+(y1-y2)**2)
	return y
print(distancia_euclidiana(x1,y1,x2,y2))
	