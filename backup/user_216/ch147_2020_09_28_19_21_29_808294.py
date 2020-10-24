def mais_frequente(lista):
    dicionario = {}
    resposta = 0
    F = 0
    for palavra in lista:
        valor = dicionario[palavra]
        if palavra not in dicionario:
            valor = 1
        else:
            valor += 1
            if valor > F:
                resposta = palavra
    return resposta
