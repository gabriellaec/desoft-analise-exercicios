def classifica_idade(x):
    if x < 11:
        return'criança'
    elif x > 12 and x < 17:
        return 'adolescente'
    else:
        return 'adulto'
