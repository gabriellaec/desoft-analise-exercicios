import math

def calcula_tempo(dic):

    dic_tempo={}

    for i in dic.keys():
        dic_tempo[i]=math.sqrt(2*100/dic[i])

    return dic_tempo