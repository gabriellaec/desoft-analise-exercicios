import math
#t=90*x/math.pi
#((v**2)/(2*9.8))*(1+(1+(2*9.8*y)/(v**2*(math.sin(t))**2)**(1/2)))*math.sin(2t)
def calcula_distancia_do_projetil(v,t,y):
    d = ((v**2)/(2*9.8))*(1+(1+(2*9.8*y)/(v**2*(math.sin(t))**2)**(1/2)))*math.sin(2*t)
    v = float(input('velocidade '))
    x = float(input('angulo '))
    t = math.pi*x/90
    y = float(input('altura inicial '))
    return d