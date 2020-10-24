def classifica_idade(idade):
    if idade <= 11:
        return 'criança'
    if idade <= 17:
        return 'adolescente'
    else:
        return 'adulto'