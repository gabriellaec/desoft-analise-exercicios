import math
def calcula_tempo(dic):
    a = len(dic)
    dc = {}
    for i in range(a):
        x = math.sqrt(200/dic[i])
        dc[i] = x
    return dc