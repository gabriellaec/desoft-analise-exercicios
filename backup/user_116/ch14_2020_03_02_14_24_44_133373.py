import math
def calcula_distancia_do_projetil(v,θ,y0):
	g=9.8
	A=(v**2)/(2*g)
	B=(1+((1+(2*g*y0)/(v**2*(math.sin(θ))**2))**0.5))
	d=A*B*math.sin(2*θ)
	return d