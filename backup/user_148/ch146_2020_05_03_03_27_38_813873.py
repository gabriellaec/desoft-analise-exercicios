def conta_ocorrencias(palavras):
    dic = {}
    lista = []
    i = 0
    while i<len(palavras):
        lista.count(palavras[i])
        dic[palavras[i]] = lista[i]
        i += 1
    return dic