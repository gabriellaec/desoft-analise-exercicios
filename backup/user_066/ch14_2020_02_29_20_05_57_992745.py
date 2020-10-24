import math
def calcula_distancia_do_projetil(v, teta, yo):
    g = 9.8
	a = (v**2/2*g)*(1+(1+(2*g*yo)/v**2*(math.sin(teta*mathpi/180))**2))*math.sin(teta*math.pi/90)
    return a