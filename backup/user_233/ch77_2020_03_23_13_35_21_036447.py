from math import sqrt

def calcula_tempo(aceleracoes):
    
    tempos = dict()
    
    for atleta in aceleracoes.keys():
        aceleracao = aceleracoes[atleta]
        tempo = sqrt(200/aceleracao)
        tempos[atleta] = tempo
    
    return tempos
    