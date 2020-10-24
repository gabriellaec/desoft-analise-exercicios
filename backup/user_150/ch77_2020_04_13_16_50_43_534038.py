from math import *
def calcula_tempo(atletas):
    dicionario_com_tempo = {}
    for nomes in atletas:
        dicionario_com_tempo[nomes] = sqrt(200/atletas[nomes]) #devolve a aceleração
    return dicionario_com_tempo