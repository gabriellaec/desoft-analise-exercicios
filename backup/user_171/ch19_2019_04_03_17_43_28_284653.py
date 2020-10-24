import math
def calcula_distancia_do_projetil(v, x, y, 6):
    g=9.8
    y=((v**2)/(g*2))*(1+(1+((2*g*y)/((v**2)*(math.sin(x)))**2)**0.5)*math.sin(2*x)
    return y
                        