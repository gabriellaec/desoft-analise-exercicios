def traduz(lista, dicionario):
    traducao= []
    for i in lista:
        traduzido= dicionario[i]
        traducao.append(traduzido)
    return traducao
        