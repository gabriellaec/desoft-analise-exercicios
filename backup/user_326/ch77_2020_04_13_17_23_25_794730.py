import math
def calcula_tempo(dicionario_nome_aceleracao):
    dicionario_nome_tempo = {}
    for nome, aceleracao in dicionario_nome_aceleracao.items():
        tempo = math.sqrt(100 * 2/ aceleracao)
        dicionario_nome_tempo[nome] = tempo
    return dicionario_nome_tempo