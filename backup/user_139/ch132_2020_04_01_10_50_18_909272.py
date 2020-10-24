import math
def calcula_trabalho (F, theta, s):
    x = math.cos(math.radians(theta))
    trabalho = F * x * s
    return trabalho