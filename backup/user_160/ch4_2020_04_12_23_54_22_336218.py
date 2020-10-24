def classifica_idade (idade):
    if idade < 11:
        return str("crianca")
    elif idade < 17:
        return str("adolescente")
    else:
        return str("adulto")