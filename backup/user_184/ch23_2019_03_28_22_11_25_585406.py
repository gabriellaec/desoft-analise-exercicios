def verifica_idade(idade):
    if idade > 17:
        return 'Liberado BRASIL'
    elif idade > 20:
        return 'Liberado EUA e BRASIL'
    else:
        return 'Não está liberado'