import math
def calcula_distancia_do_projetil(v,b,y):
    return (v**2/(2*9.8))*(1+(1+(2*(9.8*y))/v**2*(math.sin(b)**2))**(1/2))*math.sin(2*b)