import math
def calcula_tempo(dic):
    resultado_prova = {}
    for i in dic:
        tempo = math.sqrt((100*2)/dic[i])
        resultado_prova[i]=tempo
    return resultado_prova
    
