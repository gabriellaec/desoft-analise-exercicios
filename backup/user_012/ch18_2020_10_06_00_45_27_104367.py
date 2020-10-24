def verifica_idade(id):
    if id >= 21:
        return 'Liberado EUA e BRASIL'
    elif id >= 18: 
        return 'liberado BRASIL'
    else: 
        return 'Não está liberdao'