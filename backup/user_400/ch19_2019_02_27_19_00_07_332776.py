import math
def calcula_distancia_do_projetil(v, an, y):
    return (v**2/2*9.80665)*(1+(1+(2*9.80665*y)/(v**2*(math.sin(an))**2))**(1/2))*math.sin(2*an)
	
