import math
from math import cos
def calcula_trabalho (f, θ, s):
    t = f * cos(math.degrees (θ)) * s
    return t