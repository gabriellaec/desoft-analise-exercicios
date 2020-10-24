import math
atletas={'romario': 6}

def calcula_tempo(atletas):
	final={}
	for nomes, acele in atletas.items():
		t=math.sqrt(200/acele)
		final[nomes]=t
	return final
print(calcula_tempo(atletas))