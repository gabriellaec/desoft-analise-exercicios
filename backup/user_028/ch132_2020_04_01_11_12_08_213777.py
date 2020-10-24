import math
def calcula_trabalho(kg,m,seg,θ):
    F=((kg*m)/(seg**2))
    cos=math.cos(math.radians(θ))
    s=m
    τ=F*cos*s
    return τ