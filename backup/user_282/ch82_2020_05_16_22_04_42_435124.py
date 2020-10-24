def primeiras_ocorrencias(string):
    letras = dict()
    for i in string:
        if i not in letras:
            letras[i] = string.find(i)
    return letras