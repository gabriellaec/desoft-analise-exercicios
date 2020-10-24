import math 
def calcula_tempo(dic):
    dic2 = {}
    for i in dic:
        dic2[i]= math.sqrt(200/dic[i])
    return dic2
                           