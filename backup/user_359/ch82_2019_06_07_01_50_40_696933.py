def primeiras_ocorrencias(palavra):
    novo_d = {}
    for i in range(len(palavra)):
        if palavra[i] not in novo_d:
            novo_d[palavra[i]] = i
    return novo_d
