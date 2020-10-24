import math

def calcula_tempo(dic):
    result = {}
    
    for key, value in dic.items():
        result[key] = math.sqrt(200/value)
    
    return result