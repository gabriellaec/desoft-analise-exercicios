def verifica_idade(i):
    if i>=21:
        return 'Liberado EUA e BRASIL'
    elif i>=18 and i<21:
    	return 'Liberado BRASIL'
    else:
        return 'Não está liberado'
