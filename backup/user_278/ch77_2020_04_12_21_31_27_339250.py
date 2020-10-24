import math
def calcula_tempo (atletas):
    atletas_tempo = {}
    for i in atletas:
        atletas_tempo [i] = math.sqrt(200/atletas[i])   #devolve a aceleraçao
    return atletas_tempo