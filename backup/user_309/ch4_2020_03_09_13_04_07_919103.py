def classifica_idade(idd):
    if idd <= 11:
        return 'crianca'
    elif idd >= 18:
        return 'adulto'
    else:
        return 'adolescente'