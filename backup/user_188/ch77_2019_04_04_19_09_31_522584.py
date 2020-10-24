from math import sqrt

def calcula_tempo(atletas):
    tempo_de_conclusao = {}
    for nome in atletas:
        velocidade_final = sqrt(atletas[nome] * 100) 
        tempo_atleta = velocidade_final / atletas[nome]
        tempo_de_conclusao[nome] = tempo_atleta
    return tempo_de_conclusao