def verifica_idade(idade):
    if idade < 18:
        return 'Não está liberado'
    elif idade ==18 and < 21:
        return 'Liberado BRASIL'
    elif idade >= 21:
        return 'Liberado EUA e BRASIL'
    