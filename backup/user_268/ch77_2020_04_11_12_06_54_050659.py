import math
def calcula_tempo(dic):
    a = len(dic)
    dc = {}
    for i in range(a):
        x = (200/dic[i]) ** (1/2)
        dc[i] = x
    return dc