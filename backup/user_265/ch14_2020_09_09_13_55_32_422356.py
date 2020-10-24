import math
def calcula_distancia_do_projetil (v,T,y):
    d=(v**2/(2*9.8))
    e=(1+((1+(2*9.8*y))/((v**2)*(math.sin(T))**2))**(1/2)
    f=(math.sin(2*T))
    y=d*e*f
    return y