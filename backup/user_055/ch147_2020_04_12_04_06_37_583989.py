def mais_frequente(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    max_key = max(contagem, key=contagem.get)
    return max_key