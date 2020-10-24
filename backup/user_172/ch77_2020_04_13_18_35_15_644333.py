import math
def calcula_tempo(dic1):
    dic2 = {}
    for nome,t in dic1.items():
        dic2[nome] = math.sqrt(200/dic1[nome])      
    return dic2