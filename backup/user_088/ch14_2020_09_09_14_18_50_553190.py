import math
def calcula_distancia_do_projetil(v, T, y):
 d1 = (v**2)/(2*9.8)
 d2a = (1 + ( (2*9.8*y) / ((v**2)*math.sin(T)**2) ) )**(1/2)
 d2 = 1 + d2a
 d3 = math.sin(2*T)
 d = d1 * d2 * d3
 return d