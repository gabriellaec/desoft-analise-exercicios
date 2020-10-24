from math import sin
from math import sqrt
def calcula_distancia_do_projetil(y,v,a):
	d= v**2/(2*9.8)*1+sqrt(1+(2*9.8*y)/((v**2)*(sin(a)**2)))*sin(2*a)
	return d