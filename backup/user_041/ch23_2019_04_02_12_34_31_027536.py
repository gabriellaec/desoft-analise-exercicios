def verifica_idade(idade):
    if idade>21:
        return 'Liberado EUA e Brasil'
    elif idade>=18 and idade<=21:
        return 'Liberado BRASIL'
    else:
        return 'Não está liberado'