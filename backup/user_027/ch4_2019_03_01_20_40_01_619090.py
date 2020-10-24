def classifica_idade(idade):
	if int(idade) <= 11:
        return 'crianca'
    elif int(idade) <=17:
        return 'adolescente'
    else:
        return 'adulto'