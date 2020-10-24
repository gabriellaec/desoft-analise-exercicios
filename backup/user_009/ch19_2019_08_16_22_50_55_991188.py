from math import degrees, sin, sqrt

def calcula_distancia_do_projetil(v,a0,y0):
	def calcula_distancia_do_projetil(a,b,c):
	a = (v**2/2*9.8)
	b = (1+sqrt(1+((2*9.8*y0)/(v**2*(sin(a0))**2))
	c = sin(2*a0)
	d = a*b*c
	return d