def verifica_idade(idade):
    if idade >= 18:
        resposta = "Liberado no BRASIL"
    elif idade >= 21:
        resposta = "Liberado EUA e Brasil" 
    else:
        resposta = "Não está liberado"
    return resposta