import math
def calcula_trabalho(F,theta,s):
    trabalho = F * math.degrees(math.acos(math.cos(math.radians(theta)))) * s
    return trabalho

