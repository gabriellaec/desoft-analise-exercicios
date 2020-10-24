def primeiras_ocorrencias(string):
    dici = {}
    for e in string:
        if e in not in dici:
            dici[e] = 1
        else:
            dici[e] += 1
    return dici