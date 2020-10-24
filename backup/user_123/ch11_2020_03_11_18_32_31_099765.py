def distancia_euclidiana(x1,y1,x2,y2):
	b = (x1-x2)**2
	c = (y1-y2)**2
	d = (c+b)**(1/2)
	return d