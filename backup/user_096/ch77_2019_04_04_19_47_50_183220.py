import math
def calcula_tempo(dicionario):
    saida = {}
    for atleta,a in dicionario.items():
        saida[atleta] = math.sqrt(200/a)
    return saida
