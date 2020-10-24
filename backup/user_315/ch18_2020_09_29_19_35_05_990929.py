def verifica_idade(x):
    if x >= 21:
        return ('Maior no Brasil e no EUA')
    elif x == 18:
        return ('Maior no Brasil e menor no EUA')
    elif x < 18:
        return ('Menor no Brasil e no EUA')