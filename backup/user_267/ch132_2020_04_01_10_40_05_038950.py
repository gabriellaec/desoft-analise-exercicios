from math import cos, degrees
def calcula_trabalho(F,theta,s):
    trabalho = F * cos(degrees(theta)) * s
    return trabalho