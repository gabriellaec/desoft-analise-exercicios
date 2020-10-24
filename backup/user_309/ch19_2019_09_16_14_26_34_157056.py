import math

def calcula_distancia_do_projetil(v,teta,y):
	a = (v**2)/(2*g)
    b = 2*g*y
    c = (v**2)*(math.sin(teta)**2)
    d = math.sin(2**teta)
    dist = a*(1 + math.sqrt(1 + b/c))*d
    return dist
