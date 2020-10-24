import math
def calcula_distancia_do_projetil(v,yo,t):
    return (((v**2)/2*9.8)*(1+(1+(2*9.8*yo)/(v**2)*(math.sin(t))**2)**(1/2))*(math.sin(2*t)))
print (calcula_distancia_do_projetil(10,5,100))