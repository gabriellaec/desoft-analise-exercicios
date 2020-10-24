def classifica_idade(idade):
    if idade<=11:
         classificacao="crianca"
	elif idade<=17:
        classificacao="adolescente"
    else:
        classificacao="adulto"
	return classificacao
