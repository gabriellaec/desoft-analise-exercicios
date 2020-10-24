import math
def calcula_distancia_do_projetil (v,o,y):
    g=9.8
 	return ((v**2)/2*g)*(1+math.sqrt*(1+(2*g*y)/(v**2)*((math.sin(o))**2))*math.sin(2*o))