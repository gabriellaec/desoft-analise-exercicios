def distancia_euclidiana(x1,y1,x2,y2):
	x1=float(input('x1?:'))
	y1=float(input('y1?:'))
	x2=float(input('x2?:'))
	y2=float(input('y2?:'))
	dis = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
	return dis
