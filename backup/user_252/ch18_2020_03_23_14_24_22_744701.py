verifica_idade=input('Idade: '):
    if idade > 21:
        return 'Liberado EUA e BRASIL'
    elif idade >= 18:
        return 'Liberado BRASIL'
    else:
        return 'Não estã liberado'