def verifica_idade(idade):
	if idade<21 and idade>=18:
    return "Liberado BRASIL"
	if idade>=21:
    return "Liberado EUA e BRASIL"
	else:
        return "Não está liberado"