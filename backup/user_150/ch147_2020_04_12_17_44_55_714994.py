def conta_ocorrencias(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

def mais_frequente(palavra):
    lista = conta_ocorrencias(palavra).keys()
    return lista