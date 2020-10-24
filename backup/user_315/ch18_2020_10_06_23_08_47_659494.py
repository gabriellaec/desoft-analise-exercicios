def verifica_idade(idade):
    if idade >= 21:
        return 'Maior nos EUA e BRASIL'
    elif idade >= 18:
        return 'Maior no BRASIL'
    else:
        return 'Menor de idade'