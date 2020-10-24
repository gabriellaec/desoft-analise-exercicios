import math
def calcula_distancia_do_projetil(v,t,y):
    e=((v**2)/(2*9.8))
    b=((1+math.sqrt(1+(2*9.8*y)/(v**2)*(math.sin(t))**2))*(math.sin(2*t)))
    return(e*b)