from math import sin
from math import sqrt
def calcula_distancia_do_projetil(y,v,a):
	p= (v**2)/(2*9.8)
	s= sqrt(1+((2*9.8*y)/((v**2)*(sin(a)**2)))
	t= sin(2*a)
	return p*s*t