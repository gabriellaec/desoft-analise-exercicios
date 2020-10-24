from math import sqrt
def calcula_tempo(atletas_aceleracao):
    tempo_conclusao = {}
    s = 100
    for atleta, aceleracao in atletas_aceleracao.items():
        tempo_conclusao[atleta] = sqrt((2*s)/aceleracao)
    return tempo_conclusao