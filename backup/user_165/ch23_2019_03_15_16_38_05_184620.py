def verifica_idade(idade):
    if idade>21:
        return 'Liberado EUA e Brasil'
    elif idade>18:
        return 'Liberado Brasil'
    else:
        return 'Nao esta liberado'