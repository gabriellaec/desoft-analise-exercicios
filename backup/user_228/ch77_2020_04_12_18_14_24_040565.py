import math
def calcula_tempo(atletas):
    dic={}
    for n,a in atletas.items():
        t=math.sqrt(200/a)
        dic[n]=t
    return dic