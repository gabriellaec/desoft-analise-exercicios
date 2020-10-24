from math import*
def calcula_tempo(dicionario_atletas):
    dict = {}
    for atleta, aceleracao in dicionario_atletas.items():
        dict[atleta] = sqrt(200/aceleracao)
    return dict