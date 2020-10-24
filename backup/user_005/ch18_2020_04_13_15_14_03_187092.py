def verifica_idade(x):
    if x < 18:
        return ('Não está liberado')
    elif x >= 21:
        return ('Liberado EUA e BRASIL')
    else:
        return ('Liberado BRASIL')