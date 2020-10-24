import math
def calcula_tempo(dicionario):
    dicionario2={}
    
    for i in dicionario:
        if i not in dicionario2:
            dicionario2[i]=(200/dicionario[i])**1/2

    return dicionario2