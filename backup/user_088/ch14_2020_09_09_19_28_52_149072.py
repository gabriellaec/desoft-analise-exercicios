import math
def calcula_distancia_do_projetil (v ,teta , y0) :
       d1 = (v**2)/(2*9.8)
        d2=(1+ (1+ (2*9.8*y0)/((v**2)*math.sin(teta)**2))**(1/2))
        d3= math.sin(2*teta)
        d=d1*d2*d3
        return d