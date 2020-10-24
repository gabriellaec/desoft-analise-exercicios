import math
def calcula_tempo (dic_atletas):
    conclusao = {}
    for atletas in dic_atletas:
        tempo = math.sqrt(200/dic_atletas[atletas])
        conclusao[atletas] = tempo
    return conclusao