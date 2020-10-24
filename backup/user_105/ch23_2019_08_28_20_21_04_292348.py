def verifica_idade(x):
	if x > 21:
		print('Liberado EUA e BRASIL')
	elif x < 18:
		print('Não está liberado')
	else:
		print('Liberado BRASIL')