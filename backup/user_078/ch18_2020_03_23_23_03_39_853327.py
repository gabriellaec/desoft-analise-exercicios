def verifica_idade(i):
    int(i)
    if i>=21:
        return 'Liberado EUA e BRASIL'
    elif i>=18 and idade<21:
    	return 'Liberado BRASIL'
    else:
        return 'Não está liberado'
