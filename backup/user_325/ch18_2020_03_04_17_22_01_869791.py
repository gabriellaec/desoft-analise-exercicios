def verifica_idade(idade):
    if idade < 18:
        resultado = ("Não está liberado")
    elif idade >= 21:
        resultado = ("Liberado EUA e BRASIL")
    else:
        resultado = ("Liberado BRASIL")
    return resultado
print(verifica_idade(21))