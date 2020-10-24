def primeiras_ocorrencias(texto):
    indice = dict()
    for letra in texto:
        if not letra in indice:
            indice[letra] = texto[0]
    return indice