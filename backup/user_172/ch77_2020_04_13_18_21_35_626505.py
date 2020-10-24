#import math
def calcula_tempo(dic1):
    dic2 = {}
    
    for nome in dic1:
        t = dic2[nome]
        dic1[nome] = 200/t**2      
    return dic2