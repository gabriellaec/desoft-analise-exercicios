import math

def distancia_euclidiana(x2,x1,y2,y1):
	a = (x2-x1)**2
	b = (y2-y1)**2
	D = math.sqrt(a+b)
	return D