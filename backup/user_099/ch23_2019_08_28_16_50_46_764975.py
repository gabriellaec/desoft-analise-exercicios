def verifica_idade(idade):
    if idade <= 18:
        return 'Não está liberado'
    elif idade >=21:
        return 'Liberado EUA e Brasil'
    else:
        return 'Liberado Brasil'
    