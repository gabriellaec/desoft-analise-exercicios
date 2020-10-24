from math import sqrt
def calcula_tempo(dic):
    tempos = ()
    for i in dic:
		tempos[i] = sqrt(200/dic[i])
	return tempos
    