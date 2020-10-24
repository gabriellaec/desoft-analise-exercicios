from math import sqrt
teste = {'atleta1':10,'atleta2':20,'atleta3':50}

def calcula_tempo(dicionario):
    tempos = {}
    for i in dicionario:
        tempos[i] = sqrt(200/dicionario.values)
    return tempos