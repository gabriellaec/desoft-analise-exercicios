def primeiras_ocorrencias(texto):
    indice = dict()
    for i in range(len(texto)):
        if not texto[i] in indice:
            indice[texto[i]] = i
    return indice