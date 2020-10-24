def verifica_idade(idade):
    if idade>18 and idade>21:
        return 'Liberado EUA e BRASIL'
    elif idade<18:
        return 'Não está Liberado'
    else:
        return 'Liberado BRASIL'