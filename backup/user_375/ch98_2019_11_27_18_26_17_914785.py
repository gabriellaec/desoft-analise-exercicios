semestre = total_do_semestre_por_bairro(bairros)

def bairro_mais_custoso(semestre):
	valor_maior = 0.0

	for bairro, valor in semestre.items():
		if valor > valor_maior:
			valor_maior = valor
			bairro_maior = bairro
	
	return bairro_maior