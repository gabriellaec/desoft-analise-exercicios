import math 
def calcula_aceleracao(r,f):
    a= f/60 
    w= 2*math.pi*a
    ac= (w**2)*r
    return ac