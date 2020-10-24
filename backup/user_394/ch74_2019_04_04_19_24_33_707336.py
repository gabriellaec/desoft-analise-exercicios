def conta_bigramas (texto):
    dicionário = {}
    for e in texto:
        if e in dicionário:
            dicionário[e] += 1
        else:
            dicionário[e] = 1
    return dicionário