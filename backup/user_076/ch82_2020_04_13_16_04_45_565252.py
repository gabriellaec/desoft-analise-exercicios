def primeiras_ocorrencias (string):
    d = {}
    for string[n] in string:
        if string[n] not in d:
            d[string[n]] = n
        else:
            break
    return d
