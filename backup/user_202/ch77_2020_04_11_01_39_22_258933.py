import math
def calcula_tempo(atletas):
    dic = {}
    for k,v in atletas.items():
        t = math.sqrt(200/v)
        dic[k] = t
    return dic