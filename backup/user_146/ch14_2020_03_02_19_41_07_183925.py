import math
def calcula_distancia_do_projetil(v,t,yo):
    a = (v**2)/(2*9.8)
    b = math.sqrt(1+(2*9.8*yo)/(v**2*(math.sin(t))**2))
    c = math.sin(t*2)
    return (a*(1+b)*c)
print (calcula_distancia_do_projetil(10,20,30))
