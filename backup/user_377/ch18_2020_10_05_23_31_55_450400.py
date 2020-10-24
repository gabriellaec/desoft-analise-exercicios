def verifica_idade(idade):
    if idade >= 21:
        return "Maior nos Eua e Brasil"
    else:
        if idade >= 18:
            return "Maior no Brasil"
        else:
            return "Menor de idade"
