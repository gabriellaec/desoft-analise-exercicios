import math
def calcula_distancia_do_projetil (v,yo,t):
    if not v:
        return 0
    else:
    d=(((v**2)/(2*9.8))*(1+(1+(2*(9.8)*yo)/((v**2)*math.sin(t)**2))**(1/2))*(math.sin(2*t)))
    return d