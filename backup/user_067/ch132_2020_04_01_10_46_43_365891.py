import math
def calcula_trabalho(F, theta,s):
    theta = math.radians(theta)
    T = F*math.cos(theta)*s
    return T