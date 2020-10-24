import math

def calcula_aceleracao(r,f):
    hertz = f*60
    ac = (2*math.pi*hertz)**2
    ac1 = ac*r
    return ac1
