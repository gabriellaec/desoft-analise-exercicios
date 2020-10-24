import math as m
def calcula_distancia_do_projetil(v,y,tetha):
    p1 = (v**2)/(2*9.8)*(1 + m.sqrt(1 + (2*9.8*y)/((v**2)*(m.sin(tetha)**2))))*(m.sin(2*tetha))
 	return p1