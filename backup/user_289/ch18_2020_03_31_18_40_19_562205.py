def verifica_idade (idade):
    if idade >= 21:
        return ("Liberado EUA e BRASIL")
    if  idade >= 18 and idade < 21:
        return ("Liberado BRASIL")
    if idade < 18:
        return ("Não está liberado")