def verifica_idade(i):
    if i>=21:
        return 'Liberdao EUA e BRASIL'
    elif i>=18 and i<21:
        return 'LIberado BRASIL'
    else:
        return 'Não está liberado'