def verifica_idade(idd):
    if idd < 18:
        return 'Não está liberado'
    elif idd >= 21:
        return 'Liberado EUA e BRASIL'
    else:
       	return 'BRASIL'