import math
from math import cos
def calcula_trabalho (f, θ, s):
    θ_radiano = math.radians(θ)
    t = f * cos(θ_radiano) * s
    return t