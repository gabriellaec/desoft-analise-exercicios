def conta_ocorrencias (lista_palavras):
    dicio = {}
    for word in lista_palavras:
        if word in dicio:
            dicio[word] +=1
        else:
            dicio[word] =1
    return dicio


def mais_frequente (conta_ocorrencias):
    new_dicio = conta_ocorrencias(lista_palavras)
    max = 0
    for v in new_dicio.values():
        if max < v:
            max = v
    for k, v in new_dicio.items():
        if v == max:
            chave = k
    return chave