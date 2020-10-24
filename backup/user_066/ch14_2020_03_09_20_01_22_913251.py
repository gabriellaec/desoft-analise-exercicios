def calcula_distancia_do_projetil(v, teta, yo):
    g = 9.8
    fator1 = v**2/(2*g)
    fator2 = 1+(1+(2*g*yo)/(v**2*(math.sin(teta*math.pi/180))**2))**(1/2)
    fator3 = math.sin(teta*math.pi/90)
    d = fator1*fator2*fator3
    return d