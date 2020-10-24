from math import sqrt

def calcula_tempo(aceleracoes):
    
    tempos = dict()
    
    for atleta in aceleracoes.keys():
        aceleracao = aceleracoes[atleta]
        tempo = sqrt(200/aceleracao)
        tempos[atleta] = tempo
    
    return tempos

aceleracoes = dict()

while True:
    
    atleta = input()
    if atleta == 'sair': break
    aceleracao = float(input())
    
    aceleracoes[atleta] = aceleracao

tempos = calcula_tempo(aceleracoes)

tempos_lista = list(tempos.values())
atletas = list(tempos.keys())

tempo_minimo = min(tempos_lista)
indice = tempos.index(tempo_minimo)
atleta_rapido = atletas[indice]

print('O vencedor é %s com tempo de conclusão de %d s' % (atleta_rapido, tempo_minimo))



