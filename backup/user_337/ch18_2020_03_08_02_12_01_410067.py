def verifica_idade (idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    elif idade < 19:
        return 'Não está liberado'
    else:
        return 'Liberado BRASIL'
    