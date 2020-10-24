idade=5
def verifica_idade(idade):
	if idade>=21:
		return 'Liberado EUA'
	elif idade>=18:
		return 'Liberado EUA e BRASIL'
	else:
		return 'Não está liberado'
print(verifica_idade(idade))