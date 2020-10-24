def classifica_idade(idade):
    if idade <= 11:
        cal = 'crianca'
    elif idade >= 18:
        cal = 'adolescente'
    else:
        cal = 'adulto'
    return cal


