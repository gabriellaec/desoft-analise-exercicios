def classifica_idade(idade):
    if idade > 0:
        if idade < 12:
            return 'crianca'
        elif idade < 18:
            return 'adolescente'
        else:
            return 'adulto'
        