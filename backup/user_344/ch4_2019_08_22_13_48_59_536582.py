def classifica_idade(idade):
    if idade <= 11:
        return 'crianca'
    elif idade >11 and idade<18:
        return 'adolecente'
    else:
        return 'adulto'