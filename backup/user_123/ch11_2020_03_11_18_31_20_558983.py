def distancia_euclidiana(X,x,Y,y):
	b = (X-x)**2
	c = (y-y)**2
	d = (c+b)**(1/2)
	return d