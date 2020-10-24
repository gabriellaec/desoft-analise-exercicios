def calcula_distancia_projetil (v, g, y0, a):
    import math
    dist = (v**2/2*g)*(1+ math.sqrt(1+ (2*g*y0)/v**2*(math.sin(a)**2)))*math.sin(2*a)
    return dist
print(calcula_distancia_projetil(1,1,1,1))