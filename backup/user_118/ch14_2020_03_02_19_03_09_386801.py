import math
def calcula_distancia_do_projetil (v,yo,t):
    g = 9.8
    if not v:
        return 0
    else:
    return (((v**2)/(2*g))*(1+math.sqrt(1+(2*g*yo)/((v**2)*math.sin(t)**2))*(math.sin(2*t)))