import math
def calcula_trabalho(F, theta,s):
    theta = math.radians(theta)*s
    T = F*math.cos(theta)
    return T