def classifica_idade(idade):
    if idade <= 11:
        return "criança"
    elif idade <= 17:
        return "adolescente"
    elif idade >= 18:
        return "adulto"