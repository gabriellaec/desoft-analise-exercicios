import math
def calcula_tempo (dic_atletas):
    conclusao = {}
    for atletas in dic_atletas:
        acc = dic_atletas[atletas]
        tempo = math.sqrt(200/acc)
        conclusao[atletas] = tempo
    return conclusao