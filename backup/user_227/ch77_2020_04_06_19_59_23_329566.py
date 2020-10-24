from math import *
def calcula_tempo(aceleracoes):
    tempos={}
    for atleta in aceleracoes:
        tempo=sqrt((2*100)/aceleracoes[atleta])
        tempos[atleta]=tempo
    return tempos
    