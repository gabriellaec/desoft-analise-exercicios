def classifica_idade (idade):
    if 17 >= idade >= 12:
        return 'adolescente'
    elif idade >= 18:
            return 'adulto'
    else:
            return 'crianca'