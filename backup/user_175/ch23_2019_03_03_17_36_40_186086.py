def verifica_idade(idade):
    if idade >= 21:
        res = 'Liberado EUA e BRASIL'
    elif idade >= 18:
        res = 'Liberado BRASIL'
    else:
        res = 'Não está liberado'
    return res