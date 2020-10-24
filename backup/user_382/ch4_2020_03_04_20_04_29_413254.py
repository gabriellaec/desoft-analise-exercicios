def classifica_idade(idade):
	if idade <= 11:
		return ('crianca')
	elif 11<idade<18:
		return ('adolescente')
	else:
		return ('adulto')
    