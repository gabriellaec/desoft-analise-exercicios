def verifica_idade(idade):
    if idade > 21:
        return "Liberado EUA e BRASIL"
    if idade => 18:
        return "Liberado BRASIL"
    return "Não está liberado"