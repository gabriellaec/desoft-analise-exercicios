import math

def encontra_maximo(m):
	maior = 0
	for i in m[0]:
		if i**2 > maior:
			maior = i
	for i in m[1]:
		if i**2 > maior:
			maior = i
	for i in m[2]:
		if i**2 > maior:
			maior = i
	return maior
        