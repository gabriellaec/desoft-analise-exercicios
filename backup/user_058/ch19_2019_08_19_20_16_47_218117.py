import math
def calcula_distancia_do_projetil(y,v,a):
	d= v**2/(2*9.8)
    d2= 1+math.sqrt(1+(2*9.8*y)/((v**2)*(math.sin(a)**2)))
    d3= math.sin(2*a)
	return d*d2*d3