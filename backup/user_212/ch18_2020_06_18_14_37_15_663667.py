def verifica_idade (idade):
    conf = 0
    if idade < 18:
        conf = "Não está liberado"
    elif idade >= 18 and idade < 21:
        conf = "Liberado BRASIL"
    elif idade >=21:
        conf = "Liberado EUA e BRASIL"
        
    return conf