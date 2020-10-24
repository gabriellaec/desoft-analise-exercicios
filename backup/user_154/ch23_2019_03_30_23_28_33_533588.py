def verifica_idade(idade):
    if idade > 20:
        return "Liberado EUA e BRASIL"
    if idade > 17:
        return "Liberado BRASIL"
    return "Não está liberado"