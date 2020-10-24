def classifica_idade(idade):
    if idade<=11:
        return 'CRIANCA'
    elif idade>=12 and idade<=17:
        return 'ADOLESCENTE'
    else:
        return 'ADULTO'
    
    