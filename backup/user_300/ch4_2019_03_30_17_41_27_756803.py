def classifica_idade(n):
    if n < 12:
        return "crianca"
    elif n > 11 and n < 18:
        return "adolescente"
    else:
        return "adulto"