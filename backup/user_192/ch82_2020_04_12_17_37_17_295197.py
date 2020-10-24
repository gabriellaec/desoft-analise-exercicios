def primeiras_ocorrencias(texto):
    indice = dict()
    i=0
    for letra in texto:
        if not letra in indice:
            indice[letra] == texto[letra]
            i+=1
    return indice