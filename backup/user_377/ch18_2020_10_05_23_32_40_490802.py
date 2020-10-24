def verifica_idade(idade):
    if idade >= 21:
        return "Maior nos Eua e Brasil"
    elif idade >= 18:
        return "Maior no Brasil"
    else:
        return "Menor de idade"
