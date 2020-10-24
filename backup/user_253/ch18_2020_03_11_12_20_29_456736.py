def verifica_idade (idade):
    if idade <= 17:
        return("Não está liberado")
    if idade >= 18 and idade < 21:
        return ("Liberado BRASIL")
    else:
        return ("Liberado EUA e BRASIL")