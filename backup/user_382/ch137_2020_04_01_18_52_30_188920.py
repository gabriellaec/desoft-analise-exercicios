import math as m
def calcula_aceleracao(r,f):
    w = 2*m.pi*(f/60)
    ac = (w**2)*r
    return ac 
    
    