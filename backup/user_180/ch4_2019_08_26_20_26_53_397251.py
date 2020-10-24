def classifica_idade(n):
    if n <= 11:
        return str("Criança!")
    elif n >= 12 and n <= 17:
        return str("Adolescente!")
    else:
        return str("Adulto")