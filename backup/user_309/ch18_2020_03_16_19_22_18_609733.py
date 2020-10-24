def verifica_idade(idd):
    if idd < 18:
        return 'Não está liberado'
    elif idd >= 18 and idd < 21:
        return 'Liberado BRASIL'
    else:
       	return 'Liberado EUA e BRASIL'