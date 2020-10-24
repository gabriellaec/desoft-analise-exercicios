import math

g = 9.8

def calcula_distancia_do_projetil(v,teta,altura_inicial):
	a = (v**2)/(2*g)
    b = 2*g*altura_inicial
    c = v**2((math.sin(teta))**2)
	d = a*(1+((1+b/c)//2))*math.sin(2*teta)
    return d