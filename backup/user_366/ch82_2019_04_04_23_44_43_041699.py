def primeiras_ocorrencias(string):
    dici = {}
    i = 0
    for e in string:
        if e not in dici:
            dici[e] = i
        i += 1 
    return dici