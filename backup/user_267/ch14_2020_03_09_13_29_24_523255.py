def calcula_distancia_do_projetil (v, teta, yo):
    g = 9.8
    A=((v**2)/(2*g))
    B=2*g*yo
    C=(v**2)*(sin(teta))**2
    D=sin(2*teta)
    d = A*(1 + (1+(B/C))**(1/2))* D
    return d

v = 1
teta = 30
yo = 1