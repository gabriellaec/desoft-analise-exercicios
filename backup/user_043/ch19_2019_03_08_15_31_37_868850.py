def calcula_distancia_do_projetil(v,teta,y0):
    return (v**2/(2*9.8))*(1+((1+(2*9.8*y0)/((v**2)*sin(teta)**2))**(1/2))*sin(2*teta)