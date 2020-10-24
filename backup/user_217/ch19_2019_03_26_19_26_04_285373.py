import math
def calcula_distancia_do_projetil(v,an,yo):
    d= (v**2)/(2*9.8)*(1+(1+(2*9.8*yo)/(v**2)*(math.sin(an)**2))**0.5)*math.sin(2*an)
                       return d