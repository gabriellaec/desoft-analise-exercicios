def ocorrencias_letras(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        d[c] += 1
    return d