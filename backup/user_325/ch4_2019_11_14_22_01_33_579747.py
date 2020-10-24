def classifica_idade(idade):
    if idade <= 11:
        return str("crianca")
    elif idade >= 18:
        return str("adulto")
    else:
        return str("adolescente")