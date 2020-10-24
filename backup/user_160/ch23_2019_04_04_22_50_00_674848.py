def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
    else:
        if idade >= 18:
        return 'Liberado Brasil'
    else:
        return 'Não esta liberado'
    

    