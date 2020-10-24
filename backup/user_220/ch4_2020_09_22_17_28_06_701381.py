def classifica_idade(idade):
    if idade <= 11:
        resultado = "crianca"
    elif 12 >= idade <= 17:
        resultado = "adolescente"
    else:
        resultado = "adulto"
    return resultado