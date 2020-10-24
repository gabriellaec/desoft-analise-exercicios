def total_do_semestre_por_bairro(bairros):
	semestre = {}

	for bairro, meses in bairros.items():
		valor = 0.0

		for mes in meses:
			if meses.index(mes) > 5:
				valor += mes
		
		semestre[bairro] = valor

	return semestre