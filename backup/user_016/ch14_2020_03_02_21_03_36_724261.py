import math
def calcula_distancia_do_projetil(v,teta,y0):
    parte1=(v**2)/(2*9.8)
    parte2a = (2*9.8*y0)
    parte2b = ((v**2)*((math.sin(teta))**2))
    parte2 = 1 + (1 + parte2a + parte2b)**0.5
    parte3=math.sin(2*teta)
    return parte1*parte2*parte3