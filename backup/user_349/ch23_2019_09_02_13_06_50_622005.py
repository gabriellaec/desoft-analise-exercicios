def verifica_idade(i):
    if i >=18:
        if i >=21:
            return "Liberado EUA e BRASIL"
        else:
            return "Liberado BRASIL"
	if i <18:
        return "Não está liberado"