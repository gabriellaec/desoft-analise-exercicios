def primeiras_ocorrencias(string):
    dic = {letra: string.index(letra) for letra in string}
    return dic