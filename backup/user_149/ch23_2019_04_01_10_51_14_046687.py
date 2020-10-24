def verifica_idade(x):
    if x>=21:
        return 'liberado EUA e BRASIL'
    elif x>=18:
        return 'Liberado BRASIL'
    elif x<21 and x<18:
        return 'Não está liberado'