def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    elif idade <= 17 and idade >= 12:
        return "adolescente"
    else:
        return "adulto"
