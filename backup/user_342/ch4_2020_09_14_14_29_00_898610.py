def classifica_idade(idade)
    if idade<=11:
        return 'CRIANCA'
    else idade>=12 and idade<=17:
        return 'ADOLESCENTE'
    else idade>18:
        return 'ADULTO'
    
    