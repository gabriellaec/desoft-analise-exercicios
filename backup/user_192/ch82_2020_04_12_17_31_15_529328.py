def primeiras_ocorrencias(texto):
    indice = dict()
    for letra in texto:
        if not letra in indice:
            indice[letra] = letra
    return indice