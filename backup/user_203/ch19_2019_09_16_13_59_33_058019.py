from math import sin,sqrt
def calcula_distancia_do_projetil(v,teta,h):
	g=9.8
    A= (v**2)*(sin(teta))**2
    B=2*g*h
    d=(v**2)/(2*g)*(1+sqrt(1+B/A))*sin(2*teta)
    return d 