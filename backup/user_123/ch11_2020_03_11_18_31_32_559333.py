def distancia_euclidiana(X,x,Y,y):
	b = (X-x)**2
	c = (Y-y)**2
	d = (c+b)**(1/2)
	return d