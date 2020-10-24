import math
def calcula_tempo(dic1):
    dic={}
    for i,u in dic1.items():
        t=math.sqrt(200/u)
        dic[i]=t
        return dic