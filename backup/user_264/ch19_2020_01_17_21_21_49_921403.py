def calcula_distancia_do_projetil(v, teta,y0, g):
    d =(v**2/2*g)*(1+(math.sqrt((2*g*y0)/v**2*(math.sin(teta))**2)*math.sin(2*teta)
    reutrn d
g = 9.8