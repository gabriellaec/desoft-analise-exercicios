import math

def calcula_aceleracao(r,f):
    
    w = 2*math.pi*(f/60) #para deixar em rotacoes por segundo
    ac = (w**2)*r
    return ac
    
    