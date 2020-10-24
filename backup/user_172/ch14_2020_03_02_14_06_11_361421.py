import math
#calcula_distancia_do_projetil
def calcula_distancia_do_projetil(v,y,o):
    A=v**2/(2*9.8)
    B=1+math.sqrt((1+2*9.8*y)/((v**2)*(math.sin(o))**2))
    C=math.sin(o*2)
    d=A*B*C
    return d