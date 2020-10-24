from math import sqrt
teste = {'atleta1':10,'atleta2':20,'atleta3':50}

def calcula_tempo(dicionario):
    tempos = {}
    for k,v in dicionario.items():
        tempos[k] = sqrt(200/v)
    return tempos