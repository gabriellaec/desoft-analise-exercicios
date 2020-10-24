def mais_frequente(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    max_value = max(contagem.values())
    key_max_value = max_value.keys()
    return key_max_value