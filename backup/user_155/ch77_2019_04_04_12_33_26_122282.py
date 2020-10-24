import math
def calcula_tempo(dic_atletas):
    tempos = {}
    for atletas in dic_atletas:
        a = dic_atletas[atletas]
        tempo = math.sqrt(200/a)
        tempos[atleta] = tempo
	return tempo
