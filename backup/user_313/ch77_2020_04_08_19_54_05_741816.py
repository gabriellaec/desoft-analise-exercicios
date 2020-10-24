import math

def calcula_tempo(l1):
    dicionario = {}
    for k, v in l1.items():
        tempo = math.sqrt(200/v)
        dicionario[k] = tempo
        
    return dicionario