import math
def calcula_trabalho (F, O, S):
    F=F(kg*m/s**2)
    S=S(m) 
    t = F * math.degrees(math.cos(math.radians(O))) * S
    return t