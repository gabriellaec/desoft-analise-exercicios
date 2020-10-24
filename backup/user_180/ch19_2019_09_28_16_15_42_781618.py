def calcula_distancia_do_projetil(v, teta, y0):
    import math
    return ((v**2)/(2*9.8)) * (1+((1+((2*9.8)*y0)/((v**2)*(math.sin(math.radians(teta))**2))**0.5))) * (math.sin(math.radians(2*teta)))
    

