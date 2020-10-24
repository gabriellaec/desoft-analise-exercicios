def verifica_idade(idade):
    if idade >= 21:
        return 'Maior nos EUA e Brasil'
    elif idade <= 18:
        return 'Maior no Brasil'
    else:
        return 'Menor de idade'
    print(verifica_idade(17))
    print(verifica_idade(20))
    print(verifica_idade(21))
    