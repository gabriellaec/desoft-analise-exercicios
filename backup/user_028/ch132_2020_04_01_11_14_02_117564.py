import math
def calcula_trabalho(kg,m,seg,θ):
    F=((kg*m)/(seg**2))
    θ=math.cos(math.radians(θ))
    cos=θ
    s=m
    τ=F*cos*s
    return τ