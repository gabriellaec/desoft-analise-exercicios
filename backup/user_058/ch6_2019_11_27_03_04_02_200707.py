import math

def encontra_maximo(m):
	maior = (m[0][0]**2)
	for i in m[0]:
		if i**2 > maior:
			maior = i
	for i in m[1]:
		if i**2 > maior:
			maior = i
	for i in m[2]:
		if i**2 > maior:
			maior = i
	maior = math.sqrt(maior)
	return maior
        