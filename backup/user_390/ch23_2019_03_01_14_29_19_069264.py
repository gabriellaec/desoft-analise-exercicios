def verifica_idade(idade):
    if idade>20:
        return 'Liberado EUA e BRASIL'
    elif idade<18:
        return 'Não está liberado'
    else:
        return 'Liberado BRASIL'
    