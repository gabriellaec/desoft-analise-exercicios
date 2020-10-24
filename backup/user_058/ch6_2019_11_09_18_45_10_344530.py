def encontra_maximo(m):
	maior_linha = 0
	maior_coluna = 0
	maior = m[0][0]
	for l in range(3):
		for c in range(3):        
			if maior < m[l][c]:
				maior = m[l][c]
				maior_linha = l
				maior_coluna = c
	return maior
