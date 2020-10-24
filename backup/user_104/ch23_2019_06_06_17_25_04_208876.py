def verifica_idade(idade):
    if idade >= 21:
        x = 'Liberado EUA e BRASIL'
    elif idade >=18 and idade <21:
        x = 'Liberado BRASIL'
    else:
        x = 'Não está liberado'
    return x