def classifica_idade (idade):
    if 12 >= idade >= 17:
        return('adolescente')
    elif idade >= 18:
        return ('adulto')
    else:
        return ('crianca')