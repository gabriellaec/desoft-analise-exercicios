import math
def calcula_tempo(nomes_aceleracao):
    tempo_conclusao = {}
    for k, v in nomes_aceleracao.items():
        if v == 0:
            tempo_conclusao[k] = 'Não concluiu'
        else:
            tempo_conclusao[k] = math.sqrt(200/v)
    return tempo_conclusao