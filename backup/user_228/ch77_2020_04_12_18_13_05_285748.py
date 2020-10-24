import math
def calcula_tempo(atletas):
    dic={}
    for k,a in atletas.items():
        t=math.sqrt(200/a)
        dic[k]=a
    return dic