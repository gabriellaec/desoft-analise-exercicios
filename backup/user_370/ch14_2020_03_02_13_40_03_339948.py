import math

def calcula_distancia_do_projetil(v,teta,y0):
    A=(v**2)/(2*9.8)
    B=(1+(2*9.8*y0)/(v**2*(math.sin(teta))**2))**(1/2)
    C=math.sin(2*teta)
    d=A*(1+B)*C
    return(d)
    