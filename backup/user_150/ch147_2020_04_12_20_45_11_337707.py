def mais_frequente(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    lista_palavras = list(contagem.keys())
    lista_palavras2 = list(contagem.values())
    
    return lista_palavras[lista_palavras2.index(max(lista_palavras2))]