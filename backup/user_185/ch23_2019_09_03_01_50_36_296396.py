def verifica_idade(idade):
    if idade < 18:
        resposta = "Não está liberado"
    elif idade < 21:
        resposta = "Liberado no BRASIL"
    else:
        resposta = "Liberado EUA e BRASIL"
    return resposta