import math as m
def calcula_tempo(dic_atletas):
    dic={}
    for k,v in dic_atletas.items():
        t=m.sqrt(200/v)
        dic[k]=t
    return dic