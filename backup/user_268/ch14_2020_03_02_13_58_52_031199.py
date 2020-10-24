import math
def calcula_distancia_do_projetil(v, a , h):
    z = (v ** 2)/(2*9.8)
    y= 1 + math.sqrt(1 + (2 * 9.8 * h)/(v ** 2) *(math.sin(a)) ** 2)
    u= math.sin(2a)
    d= z * y * u
	return d

    