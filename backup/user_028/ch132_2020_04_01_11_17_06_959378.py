import math
def calcula_trabalho(kg,m,seg,θ):
    F=((kg*m)/(seg**2))
    angulo=math.radians(θ)
    cos=math.cos(angulo)
    s=m
    τ=F*cos*s
    return τ