def classifica_idade(perg_idade):
    y=perg_idade
    if y<=11:
        return 'crianca'
    elif y>=12 and y<=17:
        return 'adolescente'
    else:
        return 'adulto'