import math

def calcula_aceleracao(r,f):
    hz = f/60
    etapa1 = (2*math.pi*hz)
    etapa2 = etapa1**2
    ac1 = etapa2*r
    return ac1