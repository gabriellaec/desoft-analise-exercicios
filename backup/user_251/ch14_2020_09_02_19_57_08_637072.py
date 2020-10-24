import math
def distancia(v,o,y):
    x = ((v**2)/2*9.8)*(1 + math.sqrt(1 + (2*9.8*y)/(v**2)*((math.sin(o)**2))*math.sin(2*o)))
    return x


resultado = distancia(v,o,y)
print(resultado)