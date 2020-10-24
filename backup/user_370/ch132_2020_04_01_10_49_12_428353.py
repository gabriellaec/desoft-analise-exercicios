import math

def calcula_trabalho (F,teta,s):
    s= s* 57.2958
    trabalho= F * (math.sin(teta)) * s
    return trabalho