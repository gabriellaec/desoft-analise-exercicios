import math
def calcula_trabalho(F,θ,S):
    cos = math.cos(math.radians*θ)
    força = F
    distância = S
    return distância*força*cos
