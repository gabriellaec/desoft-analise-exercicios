def verifica_idade (idade):
	if idade >= 21:
		return 'Liberado EUA e Brasil'
	elif 21 > idade and idade >= 18:
		return 'Liberado Brasil'
	else:
		return 'Não está liberado'