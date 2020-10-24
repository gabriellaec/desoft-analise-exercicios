import math

def calcula_tempo(dicionario):
	tempo = {}
	for k,v in dicionario.items():
		Vf = math.sqrt(0**2 + 2*v*(100 - 0))
		t =  (Vf-0)/v
		tempo[k] = t
	return tempo