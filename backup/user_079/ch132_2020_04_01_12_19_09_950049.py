import math
def calcula_trabalho(F,a,s):
    b=math.radians(a)
    t= F*math.cos(b)*s
    J=t*s
    return J
