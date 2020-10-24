import math

def tempo(a):
    t = math.sqrt(200/a)
    return t

def calcula_tempo(dicionario):
    tempos = {}
    for atletas in dicionario:
        a = dicionario[atletas]
        t = tempo(a)
        tempos[atletas] = t
    return tempos