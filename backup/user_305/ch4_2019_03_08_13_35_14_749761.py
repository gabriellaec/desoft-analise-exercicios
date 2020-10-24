def classifica_idade(x):
    if x<= 11:
        return 'crianca'
    if x<=17 or x>=12:
        return 'adolescente'
    else:
        return 'adulto'
