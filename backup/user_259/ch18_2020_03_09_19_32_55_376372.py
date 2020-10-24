def verifica_idade(i):
    if i>=21:
        return 'Liberdao EUA e BRASIL'
    elif 18<=i and i<21:
        return 'LIberado BRASIL'
    else:
        return 'Não está liberado'