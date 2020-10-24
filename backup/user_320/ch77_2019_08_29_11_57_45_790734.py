from math import sqrt
def calcula_tempo(dic):
    tempo = {chave: sqrt(100/(valor * 2)) for chave, valor in dic.items()}
    return tempo