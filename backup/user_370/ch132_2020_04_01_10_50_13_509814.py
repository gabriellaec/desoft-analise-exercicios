import math

def calcula_trabalho (F,theta,s):
    s= s* 57.2958
    trabalho= F * (math.sin(theta)) * s
    return trabalho