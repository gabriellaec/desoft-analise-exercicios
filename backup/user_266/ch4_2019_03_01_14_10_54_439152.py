def classifica_idade(x):
    if x > 18:
        return 'adulto'
    elif x < 18 and x > 12:
        return 'adolescente'
    else:
        return 'crianca'