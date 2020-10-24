import math
from math import cos
def calcula_trabalho (f, θ, s):
    t = f * math.degrees(cos (θ)) * s
    return t