import math

def calcula_tempo(dic_atletas):
    dic_tempo_atletas = {}
    for nome, aceleracao in dic_atletas.items(): #quando se usa o items(), o primeiro "nome" é a chave a segunda "aceleracao" é o valor
        dic_tempo_atletas[nome] = math.sqrt(200/aceleracao)

    return dic_tempo_atletas
