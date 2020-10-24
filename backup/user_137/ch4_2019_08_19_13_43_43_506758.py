def classifica_idade(i):
    if i <= 11:
        return str("Crianca")
    if i >= 12 and i <= 17:
        return str("Adolescente")
    if i >= 18:
        return str("Adulto")