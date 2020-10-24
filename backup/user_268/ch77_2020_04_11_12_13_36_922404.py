import math
def calcula_tempo(dic):
    dc = {}
    for i in dic:
        x = (200/dic[i]) ** (1/2)
        dc[i] = x
    return dc