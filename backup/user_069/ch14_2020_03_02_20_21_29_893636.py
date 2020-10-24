import math
def calcula_distancia_do_projetil (v,o,y0):
    parte1 = v**2/2*9.8
    parte2 = 2*9.8*y0
    parte3 = v**2*math.sin(o)**2
    parte4 = 1 + math.sqrt(1 + parte2/parte3)
    parte5 = math.sin(2*o)
    return (parte1*parte4*parte5)