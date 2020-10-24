from math import sqrt
def calcula_tempo(dic):
    tempo = {chave: sqrt(200/valor) for chave, valor in dic.items()}
    return tempo