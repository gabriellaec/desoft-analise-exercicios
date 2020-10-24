import math

def calcula_tempo(lista):
    dict= {}
    for k, v in lista.items():
        t = math.sqrt(200/v)
        dict[k] = t
    

