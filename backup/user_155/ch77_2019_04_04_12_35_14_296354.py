import math
def calcula_tempo(dic_atletas):
    tempos = {}
    for atletas in dic_atletas:
        tempo = math.sqrt(200/dic_atletas[atletas])
        tempos[atleta] = tempo
	return tempos
