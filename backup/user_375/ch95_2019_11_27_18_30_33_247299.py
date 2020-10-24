def mais_populoso(pais):
	pop_maior = 0

	for estado in pais.values():
		pop = 0
		for populacao in estado.values():
			pop += populacao
			if pop > pop_maior:
				pop_maior = pop
				estado_maior = estado

	for k, v in pais.items():
		if v == estado_maior:
			return k