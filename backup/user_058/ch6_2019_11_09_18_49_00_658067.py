def encontra_maximo(m):
	maior = m[0][0]
	for l in range(3):
		for c in range(3):        
			if maior < m[l][c]:
				maior = m[l][c]
	return maior
