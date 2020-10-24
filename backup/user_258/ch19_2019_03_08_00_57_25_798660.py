import math
def calcula_distancia_do_projetil (v,a,y):
	d= (v**2/19.6)*(1+(1+(19.6*y/v**2*math.sin(a)**2)**0.5))*math.sin(2*a)
    return d