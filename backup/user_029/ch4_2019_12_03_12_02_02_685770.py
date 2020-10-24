def classifica_idade(x):
    if x < 12:
        return "crianca"
    if 12 < x < 18:
        return "adolescente"
    if x > 18:
        return "adulto"

