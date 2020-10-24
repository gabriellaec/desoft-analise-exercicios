import math
def calcula_distancia_do_projeto(velocidade,angulo,altura):
    y= velocidade**2/(2*9.8)*(1+ math.sqrt(1+((2*9.8*altura)/velocidade**2*(math.sen(angulo))**2)*math.sin(2*angulo)
    return y                                     