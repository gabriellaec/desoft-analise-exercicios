def primeiras_ocorrencias(string):
    dict = {}
    indice = 0
    for i in string:
        if not i in dict:
            dict[i] = indice
        indice += 1
    return dict
        