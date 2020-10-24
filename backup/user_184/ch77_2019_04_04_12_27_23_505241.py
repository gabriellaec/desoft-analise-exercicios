import math
def calcula_tempo (dic_atletas):
    conclusao = {}
    for aceleracao in dic_atletas:
        tempo = math.sqrt(200/aceleracao)
        conclusao[dic_atletas]=tempo
    return conclusao