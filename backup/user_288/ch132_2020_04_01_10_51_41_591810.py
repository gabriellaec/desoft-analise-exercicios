import math
from math import cos
def calcula_trabalho (f, θ, s):
    θ_radiano = radians(θ)
    t = f * cos(θ_radians) * s
    return t