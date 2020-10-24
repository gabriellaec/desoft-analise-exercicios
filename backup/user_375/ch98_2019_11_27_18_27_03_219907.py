def total_do_semestre_por_bairro(bairros):
	semestre = {}

	for bairro, meses in bairros.items():
		valor = 0.0

		for mes in meses:
			if meses.index(mes) > 5:
				valor += mes
		
		semestre[bairro] = valor

	return semestre

semestre = total_do_semestre_por_bairro(bairros)

def bairro_mais_custoso(semestre):
	valor_maior = 0.0

	for bairro, valor in semestre.items():
		if valor > valor_maior:
			valor_maior = valor
			bairro_maior = bairro
	
	return bairro_maior