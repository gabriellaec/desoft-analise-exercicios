def calcula_distancia_do_projetil(v,0,yo):
    d=(v**2/2*9.8)*(1 + (1 + (2*9.8*yo)/(v**2))**(1/2))
    return d
    
    