from math import cos, degrees, acos
def calcula_trabalho(F,theta,s):
    trabalho = F * degrees(acos(radians(theta))) * s
    return trabalho

