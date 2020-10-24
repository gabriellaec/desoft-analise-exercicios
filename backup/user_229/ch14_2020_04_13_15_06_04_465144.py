import math
g=9.8
def calcula_distancia_do_projetil(v,T,yo):
    d=(v**2/2*g)*(1+(1+(2*g*yo)/((v**2)*(math.sin(math.radians(T))))**2)**(1/2))*(math.sin(2*math.radians(T)))
    return d