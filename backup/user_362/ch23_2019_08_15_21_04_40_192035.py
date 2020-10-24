def verifica_idade(idade):
    if 21 >=idade >= 18:
        return "Liberado BRASIL"
    elif idade >= 21:
        return "Liberado EUA e BRASIL"
	else:
        return "Não está liberado"
        