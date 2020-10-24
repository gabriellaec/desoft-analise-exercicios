import math
g = 9.8
def  calcula_distancia_do_projetil(v,y0,x):
    a = ((v**2)/(2*g))
    b = (1 + (2 * g * y0)/((v**2)*(math.sin(x))**2))**(1/2)
    d = a * (1 + b) * math.sin(2*x)
	return d