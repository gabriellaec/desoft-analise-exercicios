def classifica_idade(idade):
    if idade >= 18:
        return 'adulto'
    else:
        if 17 >= idade >= 12:
            return 'adolescente'
        else:
            return 'crianca'