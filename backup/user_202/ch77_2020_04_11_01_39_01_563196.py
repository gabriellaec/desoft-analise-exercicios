import math
def calcula_tempo(atletas):
    dic = {}
    for k,v in atletas:
        t = math.sqrt(200/v)
        dic[k] = t
    return dic