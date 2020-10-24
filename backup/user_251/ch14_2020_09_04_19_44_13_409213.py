import math
def calcula_distancia_do_projetil(v,o,y):
    d = (v**2)/(2*9.8)*(1 + (math.sqrt(1 + (2*9.8*y)/(v**2)*(math.sin(o)**2)))*math.sin(2*o))
    return d 
    

v = 10
o = 0
y = 20

resultado = calcula_distancia_do_projetil(v,o,y,)
print(resultado)
