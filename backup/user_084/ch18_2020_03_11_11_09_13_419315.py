def verifica_idade(i):
    if i>=21:
        return('Liberado EUA e BRASIL')
    elif 21>i>=18:
        return('Liberado BRASIL')
    elif i<18:
        return('não esta liberado')