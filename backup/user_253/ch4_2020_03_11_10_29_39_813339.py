def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    elif idade > 11 and idade <= 17:
        return "adolescente"
    else:
        return "adulto"