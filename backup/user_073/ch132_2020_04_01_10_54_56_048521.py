import math
def calcula_trabalho(F,θ,s):
    θ_em_rad=math.radians(θ)
    t= F*(θ_em_rad)*s
    return t