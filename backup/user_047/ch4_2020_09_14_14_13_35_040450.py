def classifica_idade(idade):
    if idade<=11:
        return 'crianca'
    if idade > 12 and <=17:
        return 'adolescente'
    else:
        return 'adulto'