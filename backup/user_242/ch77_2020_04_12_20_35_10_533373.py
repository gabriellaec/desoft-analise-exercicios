import math as m 
def calcula_tempo(dic):
    dic2={}
    for i in dic:
        dic2[i] = m.sqrt(200/dic[i])
    return dic 2