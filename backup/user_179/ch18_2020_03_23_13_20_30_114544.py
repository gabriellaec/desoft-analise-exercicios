def verifica_idade (idade):
	if idade >= 21:
		return 'Liberado EUA e BRASIL'
	elif 21 > idade and idade >= 18:
		return 'Liberado BRASIL'
	else:
		return 'Não está liberado'