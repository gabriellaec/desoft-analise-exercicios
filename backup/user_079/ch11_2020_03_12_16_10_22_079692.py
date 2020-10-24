def distancia_euclidiana(x1,y1,x2,y2):
	x1=(input('x1?:'))
	y1=(input('y1?:'))
	x2=(input('x2?:'))
	y2=(input('y2?:'))
	dis = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
	return dis
