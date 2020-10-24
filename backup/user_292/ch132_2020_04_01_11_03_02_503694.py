import math 
def calcula_trabalho(F,θ,s):
    t=F*math.degrees(math.sin(math.radians(θ)))*s
    return t
