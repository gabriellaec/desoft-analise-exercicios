def verifica_idade(idade):
    if idade >= 21:
        a = print("Liberado EUA e BRASIL")
    if idade > 18 and idade < 21:
        a = print("Liberado BRASIL")
    else:
        a = print("Não está liberado")
    return a