import math

g = 9.8

def calcula_distancia_do_projetil(v,teta,y0):
	a= (v**2)/(2*g) 
	b= 2*g*y0
	c= (v**2)*((math.sin(teta))**2)
	d= math.sqrt(1+b/c)
	e= a*(1+math.sqrt(1+b/c))*math.sin(2*teta)
	return e
