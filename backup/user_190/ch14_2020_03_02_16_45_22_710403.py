import math
def calcula_distancia_do_projetil (yo,v,t):
    d=((v**2)/2*9.8)*(1+math.sqrt(1+(2*9.8*yo)/(v**2)*(math.sin(t))**2))*math.sin(2*t)
    return d
print(calcula_distancia_do_projetil (100,5,20))