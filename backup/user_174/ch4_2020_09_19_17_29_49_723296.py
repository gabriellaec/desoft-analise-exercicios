def classifica_idade(x):
    if x <= 11:
        return 'crianca'
    else:
        if 12<=x<= 17:
            return 'adolescente'
        else:
            if x>=18:
                return 'adulto'

