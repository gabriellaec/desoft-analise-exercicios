import math

def calcula_distancia_do_projetil(v,t,y):
	g = 9.8
    tmp1 = (v**2)/(2/g)
    tmp2 = 1 + math.sqrt(1 + (2*g*y) / ((v**2) * (math.sin(t)**2)))
    tmp3 = math.sin(2*t)
    return tmp1 * tmp2 * tmp3
    
print(calcula_distancia_do_projetil(2,30,5))