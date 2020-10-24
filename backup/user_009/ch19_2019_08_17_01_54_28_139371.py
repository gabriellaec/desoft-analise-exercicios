import from math sqrt, sin 
def calcula_distancia_do_projetil(v,a0,y0):
	q = ((v**2)/(2*9.8))*(1+(sqrt(1+((2*9.8*y0)/(v**2*(sin(a0))**2)))))*sin(2*a0)
	return q