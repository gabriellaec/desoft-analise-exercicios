import math
def calcula_distancia_do_projetil(v,O,yo):
    g=9,8
    d=(v**2/2*g)*(1+(1+2*g*yo/(v**2)*(math.sin(O))**2)**(1/2))*math.sin(2O)
    return d