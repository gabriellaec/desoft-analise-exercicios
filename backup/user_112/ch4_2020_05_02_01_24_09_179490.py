def classifica_idade(n):
    if type(n) == int:
        if n <= 11:
            return "crianca"
        elif n >= 12 and n <= 17:
            return "adolescente"
        elif n >= 18:
            return "adulto"
    