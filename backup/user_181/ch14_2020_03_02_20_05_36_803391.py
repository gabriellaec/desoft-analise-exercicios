import math
def calcula_distancia_do_projetil(v,a,y0):
    g = 9.8
    A= (v**2/(2*g))
    B = (2*g*y0)
    C = ((v**2)*(math.sin(a)**2))
    D = (1+(B/C))**.5
    E = math.sin(2*a)
    d = A * (1+D) * E
    return d