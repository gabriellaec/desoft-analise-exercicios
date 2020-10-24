def verifica_idade (idade):
    if idade > 20:
        return "Liberado EUA e BRASIL"
    if idade > 18: 
        return "Liberado BRASIL"
    else: 
        return "Não está liberado"