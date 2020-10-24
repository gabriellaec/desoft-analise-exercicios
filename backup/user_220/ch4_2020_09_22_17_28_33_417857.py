def classifica_idade(idade):
    if idade <= 11:
        resultado = "crianca"
    elif idade <= 17:
        resultado = "adolescente"
    else:
        resultado = "adulto"
    return resultado