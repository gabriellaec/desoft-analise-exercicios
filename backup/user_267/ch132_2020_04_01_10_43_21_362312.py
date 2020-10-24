from math import cos, degrees, acos, radians
def calcula_trabalho(F,theta,s):
    trabalho = F * degrees(acos(radians(theta))) * s
    return trabalho

